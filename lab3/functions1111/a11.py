#Write a Python function that checks 
# whether a word or phrase is palindrome or not. Note: A palindrome 
# is word, phrase, or sequence that reads
# the same backward as forward, e.g., madam


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("The word is a palindrome")
else:
    print("The word isnt  a palindrome")
