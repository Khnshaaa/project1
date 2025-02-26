#Write a Python program to copy the contents of a file to another file
# Function to copy file contents

import os 

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()  

        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(content)  

        print(f"File copied successfully from '{source_file}' to '{destination_file}'")

    except FileNotFoundError:
        print("Error: Source file not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"unexpected error: {e}")

source = r"C:\project1\lab6\dirandfile\example.txt"  
destination = r"C:\project1\lab6\dirandfile\copy_example.txt" 

copy_file(source, destination)
