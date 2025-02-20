#Write a Python program to find sequences of lowercase letters joined with a underscore.


import re

def finddd(text):
    pattern = r'\b[a-z]+(?:_[a-z]+)+\b'
    return re.findall(pattern, text)
text = "my-name_is khanshaiym and i_am_a_student_of_kbtu"
sequences = finddd(text)
print(sequences)
