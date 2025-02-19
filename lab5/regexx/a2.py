# 2. Write a Python program that matches a string that has an `'a'` followed by two to three `'b'`.
import re

def match_string(text):
    pattern = r'ab{2,3}$'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

print(match_string("ab"))       
print(match_string("abb"))      
print(match_string("abbb"))     
print(match_string("abbbb"))   
print(match_string("a"))    
print(match_string("abbbc"))  
