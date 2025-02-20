#Write a Python program to convert a given camel case string to snake case.
import re 
def camel_to_snake(camel_str):
    return re.sub(r'([A-Z])', r'_\1', camel_str).lower()

text = input("Enter a string: ")
print("Snake case:", camel_to_snake(text))