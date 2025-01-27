#Write a Python function that takes a 
# list and returns a new list with unique elements 
# of the first list. Note: don't use collection set.

def unique_elements():
    user_input = input("Enter elements: ")
    elements = user_input.split()
    unique_list = []
    for item in elements:
        # Add the item to the unique_list only if it's not already in it
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

result = unique_elements()
print("List with unique elements:", result)

