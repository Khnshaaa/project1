#Write a Python program to write a list to a file.
# Function to write a list to a file
import os 
def write_list_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        for item in data:
            file.write(str(item) + "\n")
    print(f"Список записан в файл '{filename}'")

data = ["Python", "Java", "C++", "JavaScript"]
write_list_to_file(r"C:\project1\lab6\dirandfile\languages.txt", data)
