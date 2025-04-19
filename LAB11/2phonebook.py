# phonebook.py с комментариями для лучшего понимания

import psycopg2  # библиотека для работы с PostgreSQL
import csv       # библиотека для чтения CSV файлов
from tabulate import tabulate  # для красивого вывода таблиц в консоли

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="contacts",
    user="postgres",
    password="12345678"
)
cur = conn.cursor()  # создаем курсор для выполнения SQL-запросов
#execute(...) — отправляет SQL-запрос.
# Функция для создания таблицы Users, если она не существует

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(50),
            user_phone VARCHAR(20)
        );
    """)
    conn.commit()
    print("Таблица создана или уже существует.")

# Вставка пользователя вручную с консоли

def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    cur.execute("INSERT INTO Users (user_name, user_phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Пользователь добавлен.")

# Вставка пользователей из CSV файла

def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO Users (user_name, user_phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Данные из CSV загружены.")

# Обновление данных пользователя

def update_user():
    old_name = input("Введите имя пользователя для обновления: ")
    new_name = input("Новое имя (Enter, если без изменений): ")
    new_phone = input("Новый номер (Enter, если без изменений): ")

    if new_name:
        cur.execute("UPDATE Users SET user_name = %s WHERE user_name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE Users SET user_phone = %s WHERE user_name = %s", (new_phone, new_name or old_name))
    conn.commit()
    print("Данные пользователя обновлены.")

# Удаление пользователя по имени или номеру

def delete_user():
    key = input("Введите имя или номер для удаления: ")
    cur.execute("DELETE FROM Users WHERE user_name = %s OR user_phone = %s", (key, key))
    conn.commit()
    print("Пользователь удалён.")

# Поиск пользователя по имени или номеру (регистр не важен)

def search_users():
    filter_value = input("Введите имя или номер для поиска: ")
    cur.execute(
        "SELECT * FROM Users WHERE user_name ILIKE %s OR user_phone LIKE %s", 
        (f"%{filter_value}%", f"%{filter_value}%")
    )
    results = cur.fetchall()
    print(tabulate(results, headers=["ID", "Имя", "Телефон"], tablefmt="grid"))

# Вывод всех пользователей

def show_all_users():
    cur.execute("SELECT * FROM Users")
    results = cur.fetchall()
    if results:
        print(tabulate(results, headers=["ID", "Имя", "Телефон"], tablefmt="grid"))
    else:
        print("Контакты не найдены.")

# Создание хранимых функций и процедур

def create_functions_and_procedures():
    # Удаляем, если уже есть
    cur.execute("DROP FUNCTION IF EXISTS search_by_pattern(TEXT);")
    cur.execute("DROP PROCEDURE IF EXISTS insert_or_update_user(TEXT, TEXT);")
    cur.execute("DROP FUNCTION IF EXISTS insert_many_users(TEXT[], TEXT[]);")
    cur.execute("DROP FUNCTION IF EXISTS get_users_paginated(INT, INT);")
    cur.execute("DROP PROCEDURE IF EXISTS delete_by_name_or_phone(TEXT);")

    # 1. Поиск по шаблону
    #LANGUAGE plpgsql — это язык функций в PostgreSQL (аналог Python, но для БД).
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
    """)
    #Внутри этих $$ ... $$ пишется тело процедуры.
    #END; — завершение тела функции.
    # 2. Вставка или обновление
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
    """)

    # 3. Массовая вставка
    cur.execute(r"""
    CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], phones TEXT[])
    RETURNS TEXT[] AS $$
    DECLARE
        i INT;
        bad_entries TEXT[] := '{}';
    BEGIN
        FOR i IN 1..array_length(names, 1) LOOP
            IF phones[i] ~ '^\\+?\\d{6,15}$' THEN
                CALL insert_or_update_user(names[i], phones[i]);
            ELSE
                bad_entries := array_append(bad_entries, names[i] || ' - ' || phones[i]);
            END IF;
        END LOOP;
        RETURN bad_entries;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # 4. Пагинация
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
    """)

    # 5. Удаление по ключу
    cur.execute(r"""
    CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(key TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM Users WHERE user_name = key OR user_phone = key;
    END;
    $$;
    """)

    conn.commit()
    print("Функции и процедуры созданы.")

# Обёртки для вызова процедур/функций

def search_by_pattern_console():
    pattern = input("Введите шаблон для поиска: ")
    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    results = cur.fetchall()
    print(tabulate(results, headers=["ID", "Имя", "Телефон"], tablefmt="grid"))

def insert_or_update_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print("Вставка или обновление выполнены.")

def insert_many_console():
    count = int(input("Сколько пользователей добавить? "))
    names, phones = [], []
    for _ in range(count):
        names.append(input("Имя: "))
        phones.append(input("Телефон: "))
    cur.execute("SELECT insert_many_users(%s, %s);", (names, phones))
    bad = cur.fetchone()[0]
    print("Неправильные записи:", bad)
    conn.commit()

def get_users_paginated_console():
    lim = int(input("Сколько записей (лимит): "))
    off = int(input("Смещение (offset): "))
    cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (lim, off))
    results = cur.fetchall()
    print(tabulate(results, headers=["ID", "Имя", "Телефон"], tablefmt="grid"))

def delete_by_key_console():
    key = input("Введите имя или номер для удаления: ")
    cur.execute("CALL delete_by_name_or_phone(%s);", (key,))
    conn.commit()
    print("Удаление выполнено.")

# Главное меню

def menu():
    create_table()
    create_functions_and_procedures()

    while True:
        print("\nМеню:")
        print("1. Вставить данные (с консоли)")
        print("2. Вставить данные (из CSV)")
        print("3. Обновить пользователя")
        print("4. Удалить пользователя")
        print("5. Поиск пользователя")
        print("6. Показать все контакты")
        print("7. Выход")
        print("8. Поиск по шаблону (SP Func)")
        print("9. Вставка или обновление (SP Proc)")
        print("10. Массовая вставка (Func)")
        print("11. Показать с пагинацией (SP Func)")
        print("12. Удалить по имени/номеру (SP Proc)")

        choice = input("Ваш выбор: ")

        if choice == "1": insert_from_console()
        elif choice == "2": insert_from_csv(input("Путь к CSV: "))
        elif choice == "3": update_user()
        elif choice == "4": delete_user()
        elif choice == "5": search_users()
        elif choice == "6": show_all_users()
        elif choice == "7": break
        elif choice == "8": search_by_pattern_console()
        elif choice == "9": insert_or_update_console()
        elif choice == "10": insert_many_console()
        elif choice == "11": get_users_paginated_console()
        elif choice == "12": delete_by_key_console()
        else: print("Неверный выбор!")

    cur.close()
    conn.close()

# Точка входа
if __name__ == "__main__":
    menu()
