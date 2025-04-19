import psycopg2

def search_user_by_name_part(part_of_name):
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

        # SQL запрос с использованием LIKE для поиска по части имени
        query = """
        SELECT * FROM users WHERE user_name LIKE %s;
        """
        part_of_name = f"%{part_of_name}%"  # добавляем % в начале и в конце для поиска по подстроке
        cursor.execute(query, (part_of_name,))

        # Выводим результаты
        users = cursor.fetchall()
        for user in users:
            print(f"User ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}")
        
        # Закрытие соединения
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

# Пример использования
search_user_by_name_part("Алекс")  # Найдет все имена, содержащие "Алекс"
