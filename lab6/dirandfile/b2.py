#Write a Python program to check for access to a specified path. Test the existence, readability, 
# writability and executability of the specified path


import os
path = input("Enter the path: ")
if os.path.exists(path):
    print(f"Exists: Yes")
    print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
    print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
    print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
else:
    print("The specified path does not exist.")

#"C:\project1\lab6\dirandfile\alphabet.txt"
