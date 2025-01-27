#Write a function that accepts string 
# from user and print all permutations of that string.

'''
def print_unique_permutations():
    user_input = input("Enter a string: ")

    # Generate all unique permutations of the string by using a set
    unique_permutations = set(itertools.permutations(user_input))

    # Print each unique permutation
    for perm in unique_permutations:
        print(''.join(perm))

# Example usage:
print_unique_permutations()

'''

def generate_permutations(string, current_index=0):
    # Base case: if current_index reaches the end of the string, print the permutation
    if current_index == len(string):
        print(''.join(string))
        return
    
    # Recursive case: generate permutations by swapping each character with the current_index
    for i in range(current_index, len(string)):
        # Swap the character at current_index with character at i
        string[current_index], string[i] = string[i], string[current_index]
        
        # Recursively call to permute the rest of the string (from current_index + 1 onwards)
        generate_permutations(string, current_index + 1)
        
        # Backtrack: swap the characters back to restore the original order
        string[current_index], string[i] = string[i], string[current_index]

def print_permutations():
    # Get the input string from the user
    user_input = input("Enter a string: ")
    
    # Convert the string to a list for easier manipulation (because strings are immutable)
    string_list = list(user_input)
    
    # Start the recursive permutation generation
    generate_permutations(string_list)

# Example usage:
print_permutations()
