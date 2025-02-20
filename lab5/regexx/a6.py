#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re          
text = input("Enter  a text: ")
result = re.sub(r'[ ,.]', ':', text)
print("Modified text:", result)