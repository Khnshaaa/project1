#Write a program which can filter prime numbers in a
# list by using filter function. Note: Use lambda to
# define anonymous functions.



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 50))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)  
