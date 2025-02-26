#Write a Python program to list only directories, files 
# and all directories, files in a specified path.

# import os

# current_directory = os.getcwd()
# print("Current Directory:", current_directory)



import os      
path = input("the way to dirctory: ")

if not os.path.exists(path):
    print("this way doesnt exist")
else:
    all_items = os.listdir(path)
    directories = [item for item in all_items  if os.path.isdir(os.path.join(path , item))]
    
    files = [item  for item in all_items if os.path.isfile(os.path.join(path , item ))]
    
    print("directories: " , directories)
    print("files: " , files)
    print("allitem: " , all_items)
    

