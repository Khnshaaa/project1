#Write a program to solve a classic puzzle: 
# We count 35 heads and 94 legs among the chickens 
# and rabbits in a farm. How many rabbits and how many
# chickens do we have? 
# create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    # x + y = numheads
    # 2x + 4y = numlegs
    if (4 * numheads - numlegs) % 2 != 0 or (numlegs % 2 != 0):
        return "No solution exists."
    
    chickens = (4 * numheads - numlegs) // 2
    rabbits = numheads - chickens
    
    if chickens < 0 or rabbits < 0:
        return "No solution exists."
    
    return chickens, rabbits

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

#isinstance() is used to verify that the result is a tuple, which means 

# the function has returned a valid answer (the number of chickens and rabbits).

if isinstance(result, tuple):
    print(f"Number of chickens: {result[0]}, Number of rabbits: {result[1]}")
#Tuples are perfect when you need to return multiple related values. In this case, 
# we need to return both the number of chickens and rabbits.
else:
    print(result)
