# 2. Write a Python program that matches a string that has an `'a'` followed by two to three `'b'`.
import re

a = r'^ab{2,3}$'
b = input().split()

for i in b:
    if re.fullmatch(a, i):
        print("true")
    else: print("false")
