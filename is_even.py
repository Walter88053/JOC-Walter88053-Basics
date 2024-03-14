# Testing for even or odd by Writing a Function
# John Kowal  -  WALTER$

import math

def is_even():
    num1 = eval(input("Enter a number:  "))
    remainder = num1 % 2
    if remainder == 0:
        print(num1, "is even")
    else:
        print(num1, "is odd")

def main():
    is_even()
    is_even()

main()
