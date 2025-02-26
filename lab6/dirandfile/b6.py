#Write a Python program to generate 26 
# text files named A.txt, B.txt, and so on up to Z.txt


import os
import string  

directory = r"C:\project1\lab6\dirandfile\alphabet.txt"

os.makedirs(directory, exist_ok=True)

for letter in string.ascii_uppercase:  
    filename = os.path.join(directory, f"{letter}.txt")  
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"This is file {letter}.txt\n")

print("26 text files (A.txt to Z.txt) created successfully!")
