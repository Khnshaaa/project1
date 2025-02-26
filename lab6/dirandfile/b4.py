#Write a Python program to count the number of lines in a text file.
# Function to count lines in a file
# Write a Python program to count the number of lines in a text file.
# Function to count lines in a file
import os 

def count_lines(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            lines = file.readlines()  
            return len(lines) 
    except FileNotFoundError:
        print("File not found!")
        return None
    except PermissionError:
        print("Permission denied! You don't have access to this file.")
        return None

filename = r"C:\project1\lab6\dirandfile\example.txt" 
line_count = count_lines(filename)

if line_count is not None:
    print(f"Total number of lines: {line_count}") 
