#Create a python file and import 
# some of the functions from the above 13 tasks 
# and try to use them.

from functions1111 import is_polinderome

words=['apple','banana','alaala','data','elderberry','apple','banana']
for i in words:
    if is_polinderome(i):
        print(i)
    else:
        print('not a palindrome')   
    
