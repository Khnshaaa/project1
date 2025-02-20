#Write a Python program to split a string at uppercase letters.
import re 
text = input("Enter a string: ")
words = re.findall(r'[A-Z][a-z]*', text)
print( words)
