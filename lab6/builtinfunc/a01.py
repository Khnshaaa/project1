#Write a Python program with builtin function 
# to multiply all the numbers in a list

from functools import reduce 
import operator 

def multiply_list(numbers):
    return reduce (operator.mul , numbers)

numbers = list(map(int , input ().split()))
result = multiply_list(numbers)
print (result)
