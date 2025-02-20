#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re           
pattern = r'\b[A-Z][a-z]+\b'
text = input("Enter text: ")
matches = re.findall(pattern, text)

print("Matches:", matches)