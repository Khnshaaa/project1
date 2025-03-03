import json 

students = [
    {"name": "Kahnshaiiym", "age": 18, "grade": 2},
    {"name": "Alice", "age": 19, "grade": 3},
    {"name": "Bob", "age": 20, "grade": 4}
]

# Записываем список в файл
with open("students.json", "w") as file:
    json.dump(students, file)

# Читаем из файла
with open("students.json", "r") as file:
    data = json.load(file)
    
# Выводим только имена студентов
for student in data:
    print(student["name"])
