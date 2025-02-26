#Write a Python program to delete file by specified path. Before deleting check for access
# and whether a given path exists or not.
import os
def delete_file(file_path):
    try:
        if not os.path.exists(file_path):
            print("Error: File does not exist!")
            return
        
        if not (os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK)):
            print("Error: File is not accessible (read/write permissions required)!")
            return
        
        os.remove(file_path)
        print(f"✅ File '{file_path}' has been deleted successfully!")

    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"Unexpected error: {e}")

file_to_delete = input("Enter the full path of the file to delete: ").strip()

delete_file(file_to_delete)


#"C:\project1\lab6\dirandfile\example.txt"