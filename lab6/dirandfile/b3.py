#Write a Python program to test whether a given path exists or not. If the path exist find the 
# filename and directory portion of the given path.
import os

path = "C:/project1"

if os.path.exists(path):
    print("The path exists!")
    directory = os.path.dirname(path)  
    filename = os.path.basename(path)  

    print(f"Directory: {directory}")
    print(f"File Name: {filename}" if filename else "This is a directory, not a file.")
else:
    print("The path does not exist.")
