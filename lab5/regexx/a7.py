#Write a python program to convert snake case string to camel case string.
import re           

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

text = input("Enter a string: ")
print( snake_to_camel(text))