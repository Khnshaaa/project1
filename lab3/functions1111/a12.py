#Define a functino histogram() that takes 
# a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:

#****
#*********
#*******

def histogram(lll):
    for num in lll:
        print('*' * num)

histogram([4, 9, 7])
