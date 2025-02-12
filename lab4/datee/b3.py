#Write a Python program to drop microseconds from datetime.

from datetime import datetime

now = datetime.now()
without_micro = now.replace(microsecond=0)
print("With microseconds:    ", now)
print("Without microseconds: ", without_micro)
