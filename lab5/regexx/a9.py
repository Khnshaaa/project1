#Write a Python program to insert spaces between words starting with capital letters.

import re


text = input("Enter a string: ")
result = re.sub(r'([A-Z])', r' \1', text).strip()

print("Modified text:", result)