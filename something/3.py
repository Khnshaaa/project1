#Реализуй функцию сортировки пользователей по имени или телефону перед их выводом.

import psycopg2

# Соединение с базой данных
conn = psycopg2.connect("dbname=test user=postgres password=secret")
cur = conn.cursor()

# Выполним запрос
cur.execute("SELECT user_name, user_age FROM users")

# Получим все строки
rows = cur.fetchall()

# Сортируем данные по возрасту
sorted_rows = sorted(rows, key=lambda x: x[1])  # Сортировка по возрасту (второй элемент кортежа)

# Выводим отсортированные данные
for row in sorted_rows:
    print(row)

# Закрытие соединения
cur.close()
conn.close()
