#Write a Python program to check for access to a specified path. Test the existence, readability, 
# writability and executability of the specified path


import os
path = input("Enter the path: ")
if os.path.exists(path):
    print(f"✅ Exists: Yes")
    print(f"📖 Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
    print(f"✍ Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
    print(f"⚡ Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
else:
    print("❌ The specified path does not exist.")








# print("\u2705 Exists")  # ✅ Check mark
# print("\U0001F4D6 Readable")  # 📖 Open book
# print("\U0000270F Writable")  # ✍ Pencil
# print("\U000026A1 Executable")  # ⚡ Lightning
# print("\U0000274C Not Found")  # ❌ Red cross
