#Write a program using generator to 
# print the even numbers between 0 and n 
# in comma separated form 
# where n is input from console.


def even_numbers(n):
    even_nums = []  
    for num in range(0, n+1, 2):  
        even_nums.append(num)  
    return even_nums 

n = int(input())
even_nums_list = even_numbers(n)

# Print the even numbers in comma-separated form
print(", ".join(map(str, even_nums_list)))
