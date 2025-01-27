#Write a function that takes in a list of integers and returns True if it contains 007 in order
#def spy_game(nums):
#    pass

#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    seq = [0, 0, 7]
    idx = 0 

    for num in nums:
        # Check if the current number matches the current sequence element
        if num == seq[idx]:
            idx += 1 
        if idx == len(seq):
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  
