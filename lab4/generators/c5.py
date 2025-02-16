#Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    for i in range(n, -1, -1):
        yield i

a=int(input())
for number in countdown(a):
    print(number)
