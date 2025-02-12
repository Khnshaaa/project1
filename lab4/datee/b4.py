#Write a Python program to calculate 
# two date difference in seconds.

from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0)  
date2 = datetime(2024, 2, 12, 14, 30, 0)  
#year month day hour minute seconds 
difference = date2 - date1

seconds_difference = difference.total_seconds()
print("Difference in seconds:", seconds_difference)
