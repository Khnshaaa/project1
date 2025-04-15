
# # lab10/phonebook.py
import psycopg2
import csv
from tabulate import tabulate

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
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
    key = input("Enter name or phone number to delete: ")
    cur.execute("DELETE FROM Users WHERE user_name = %s OR user_phone = %s", (key, key))
    conn.commit()
    print("User deleted.")

# Search users by name or phone (case-insensitive)
def search_users():
    filter_value = input("Enter name or phone number to search: ")
    cur.execute("SELECT * FROM Users WHERE user_name ILIKE %s OR user_phone LIKE %s", 
                (f"%{filter_value}%", f"%{filter_value}%"))
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

# Main menu loop
def menu():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Insert data (from console)")
        print("2. Insert data (from CSV)")
        print("3. Update user")
        print("4. Delete user")
        print("5. Search user")
        print("6. Show all contacts")
        print("7. Exit")

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
        else:
            print("Invalid choice!")

    # Close cursor and connection after exiting the loop
    cur.close()
    conn.close()

# Entry point
if __name__ == "__main__":
    menu()
