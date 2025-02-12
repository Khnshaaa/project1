# Write a Python program to calculate 
# the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math

def rarea(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return int(area) if area.is_integer() else area

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = rarea(n, s)
print(f"The area of the polygon is: {area:.1f}")

