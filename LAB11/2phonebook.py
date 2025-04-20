# # lab10/phonebook.py
import psycopg2
import csv
from tabulate import tabulate

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="contacts",
    user="postgres",
    password="12345678"
)
cur = conn.cursor()

# Create the Users table if it does not exist
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(50),
            user_phone VARCHAR(20)
        );
    """)
    conn.commit()
    print("Table created or already exists.")

# Insert user from console input
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO Users (user_name, user_phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("User added.")

# Insert users from a CSV file
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO Users (user_name, user_phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data from CSV has been loaded.")

# Update existing user information
def update_user():
    old_name = input("Enter the name of the user to update: ")
    new_name = input("Enter new name (press Enter to skip): ")
    new_phone = input("Enter new phone number (press Enter to skip): ")

    if new_name:
        cur.execute("UPDATE Users SET user_name = %s WHERE user_name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE Users SET user_phone = %s WHERE user_name = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("User data updated.")

# Delete user by name or phone
def delete_user():
    key = input("Enter name or phone number  or id  to delete: ")
    cur.execute("DELETE FROM Users WHERE user_name = %s OR user_phone = %s OR user_id = %s " , (key, key , key ))
    conn.commit()
    print("User deleted.")

# Search users by name or phone (case-insensitive)
def search_users():
    filter_value = input("Enter name or phone number to search: ")
    cur.execute(
        "SELECT * FROM Users WHERE user_name ILIKE %s OR user_phone LIKE %s", 
        (f"%{filter_value}%", f"%{filter_value}%")
    )
    results = cur.fetchall()
    print(tabulate(results, headers=["ID", "Name", "Phone"], tablefmt="grid"))

# Show all users in the table
def show_all_users():
    cur.execute("SELECT * FROM Users")
    results = cur.fetchall()
    if results:
        print(tabulate(results, headers=["ID", "Name", "Phone"], tablefmt="grid"))
    else:
        print("No contacts found.")

# === Create or replace stored functions and procedures in DB ===
def create_functions_and_procedures():
    # Drop existing definitions to avoid conflicts
    cur.execute("DROP FUNCTION IF EXISTS search_by_pattern(TEXT);")
    cur.execute("DROP PROCEDURE IF EXISTS insert_or_update_user(TEXT, TEXT);")
    cur.execute("DROP PROCEDURE IF EXISTS insert_many_users(TEXT[], TEXT[], TEXT[]);")
    cur.execute("DROP FUNCTION IF EXISTS get_users_paginated(INT, INT);")
    cur.execute("DROP PROCEDURE IF EXISTS delete_by_name_or_phone(TEXT);")
    

    # 1. search_by_pattern function
    # Внутри этих $$ ... $$ пишется тело процедуры.
    #Всё, что выполняется внутри процедуры, оборачивается в BEGIN ... END;.
    cur.execute(r"""
    CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
    RETURNS TABLE(user_id INT, user_name VARCHAR, user_phone VARCHAR) AS $$ 
    BEGIN 
        RETURN QUERY 
        SELECT u.user_id, u.user_name, u.user_phone 
        FROM Users u 
        WHERE u.user_name ILIKE '%' || pattern || '%' 
        OR u.user_phone LIKE '%' || pattern || '%'; 
    END; 
    $$ LANGUAGE plpgsql;
    """
    )

    # 2. insert_or_update_user procedure
    cur.execute(r"""
    CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, phone TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM Users WHERE user_name = name) THEN
            UPDATE Users SET user_phone = phone WHERE user_name = name;
        ELSE
            INSERT INTO Users(user_name, user_phone) VALUES (name, phone);
        END IF;
    END;
    $$;
    """
    )

    # 3. insert_many_users function returning bad entries with relaxed regex
    cur.execute(r"""
    CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], phones TEXT[])
    RETURNS TEXT[] AS $$
    DECLARE
        i INT;
        bad_entries TEXT[] := '{}';
    BEGIN
        FOR i IN 1..array_length(names, 1) LOOP
            -- now allow phone numbers from 6 to 15 digits, optional +
            IF phones[i] ~ '^\+?\d{6,15}$' THEN
                CALL insert_or_update_user(names[i], phones[i]);
            ELSE
                bad_entries := array_append(bad_entries, names[i] || ' - ' || phones[i]);
            END IF;
        END LOOP;
        RETURN bad_entries;
    END;
    $$ LANGUAGE plpgsql;
    """
    )

    # 4. get_users_paginated function returning SETOF Users
    cur.execute(r"""
    CREATE OR REPLACE FUNCTION get_users_paginated(limit_num INT, offset_num INT)
    RETURNS SETOF Users AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM Users
        ORDER BY user_id
        LIMIT limit_num OFFSET offset_num;
    END;
    $$ LANGUAGE plpgsql;
    """
    )

    # 5. delete_by_name_or_phone procedure
    cur.execute(r"""
    CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(key TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM Users WHERE user_name = key OR user_phone = key;
    END;
    $$;
    """
    )

    conn.commit()
    print("Stored functions and procedures created successfully.")

# Wrappers for calling stored procedures/functions from Python

def search_by_pattern_console():
    pattern = input("Enter pattern to search: ")
    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    results = cur.fetchall()
    print(tabulate(results, headers=["ID", "Name", "Phone"], tablefmt="grid"))


def insert_or_update_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print("Insert or update executed.")


def insert_many_console():
    count = int(input("How many users to insert? "))
    names, phones = [], []
    for _ in range(count):
        names.append(input("Name: "))
        phones.append(input("Phone: "))
    # Call function and fetch bad entries
    cur.execute("SELECT insert_many_users(%s, %s);", (names, phones))
    bad = cur.fetchone()[0]
    print("Bad entries:", bad)
    conn.commit()


def get_users_paginated_console():
    lim = int(input("Limit: "))
    off = int(input("Offset: "))
    cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (lim, off))
    results = cur.fetchall()
    print(tabulate(results, headers=["ID", "Name", "Phone"], tablefmt="grid"))


def delete_by_key_console():
    key = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_by_name_or_phone(%s);", (key,))
    conn.commit()
    print("Delete procedure executed.")

# Main menu loop
def menu():
    create_table()
    create_functions_and_procedures()

    while True:
        print("\nMenu:")
        print("1. Insert data (from console)")
        print("2. Insert data (from CSV)")
        print("3. Update user")
        print("4. Delete user")
        print("5. Search user")
        print("6. Show all contacts")
        print("7. Exit")
        print("8. Search by pattern (SP Func)")
        print("9. Insert or update user (SP Proc)")
        print("10. Insert many users (Func)")
        print("11. Show paginated users (SP Func)")
        print("12. Delete by name/phone (SP Proc)")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            path = input("Enter path to CSV file: ")
            insert_from_csv(path)
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            search_users()
        elif choice == "6":
            show_all_users()
        elif choice == "7":
            break
        elif choice == "8":
            search_by_pattern_console()
        elif choice == "9":
            insert_or_update_console()
        elif choice == "10":
            insert_many_console()
        elif choice == "11":
            get_users_paginated_console()
        elif choice == "12":
            delete_by_key_console()
        else:
            print("Invalid choice!")

    cur.close()
    conn.close()

# Entry point
if __name__ == "__main__":
    menu() 