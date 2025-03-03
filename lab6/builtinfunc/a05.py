#Write a Python program with builtin function that returns True 
# if all elements of the tuple are true.


def all_elements_true(t):
    return all(t) if t else False 


user_input = input("Enter tuple elements separated by spaces: ").split()
user_tuple = tuple(
    True if x.lower() == "true" else 
    False if x.lower() == "false" else 
    int(x) if x.isdigit() else x 
    for x in user_input
)
result = all_elements_true(user_tuple)

print(result)
