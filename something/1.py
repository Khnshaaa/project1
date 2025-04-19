
#Напиши функцию для экспорта всех данных пользователей из базы данных в CSV файл.


import psycopg2
import csv

def insert_users_from_csv(file_path):
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname="your_db_name", 
            user="your_db_user", 
            password="your_db_password", 
            host="your_db_host", 
            port="your_db_port"
        )
        cursor = conn.cursor()

        # Открытие CSV файла и чтение данных
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                user_name = row[0]
                user_phone = row[1]
                
                # Проверка на дубликаты по имени или телефону
                cursor.execute("SELECT COUNT(*) FROM users WHERE user_name = %s OR user_phone = %s", (user_name, user_phone))
                count = cursor.fetchone()[0]
                
                if count == 0:  # Если нет дубликатов, вставляем запись
                    cursor.execute("INSERT INTO users (user_name, user_phone) VALUES (%s, %s)", (user_name, user_phone))
                    print(f"Added: {user_name} - {user_phone}")
                else:
                    print(f"Duplicate found: {user_name} - {user_phone}, skipping.")

        # Сохранение изменений в базе данных
        conn.commit()
        print("Mass insert completed.")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()

# Пример использования
insert_users_from_csv("users.csv")
