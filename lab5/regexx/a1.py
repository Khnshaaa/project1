# 1. Write a Python program that matches a string that has an `'a'` followed by zero or more `'b'`'s.
# import re

# def match_string(text):
#     pattern = r'ab*'
#     if re.fullmatch(pattern, text):
#         return True
#     else:
#         return False

# print(match_string("a"))        
# print(match_string("ab"))       
# print(match_string("abb"))      
# print(match_string("ac"))       
# print(match_string("abc")) 

import re

def match_string(s):
    pattern = r'^ab*$'
    return bool(re.fullmatch(pattern, s))
user_input = input("Enter a string: ")

if match_string(user_input):
    print("The string matches ")
else:
    print("The string does not match")
