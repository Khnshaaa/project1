#Write a Python program to convert degree to radian.
#Input degree: 15
#Output radian: 0.261904
import math
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print(f"Output radian: {radian:.6f}")
