# Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
import math

def parea(base, height):
    return base * height
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = parea(base, height)
print(f"Expected Output: {area:.1f}")
