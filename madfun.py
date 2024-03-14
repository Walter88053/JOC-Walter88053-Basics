# Madfun
# Enter a number and return the absolute value,
# the number rounded to 0 decimal places, and the square root.
# John Kowal  -  WALTER$

import math
from math import sqrt

num = eval(input("Please enter your number: "))

print("The absolute value of your number is", abs(num))
print("Your number rounded to 0 decimal places is", round(num, 0))
print("The square root of your number is", math.sqrt(abs(round(num, 0))))