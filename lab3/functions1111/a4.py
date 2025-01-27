#You are given list of numbers separated by spaces. 
# Write a function filter_prime which
# will take list of numbers as an agrument
# and returns only prime numbers from the list.


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    # Use the is_prime function to filter out prime numbers
    return [num for num in numbers if is_prime(num)]

# Example Usage:
numbers = list(map(int, input("Enter numbers :  ").split()))

prime_numbers = filter_prime(numbers)

print("Prime numbers:", prime_numbers)
