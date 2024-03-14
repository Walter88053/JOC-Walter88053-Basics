# Calculate Total Meal Cost by Writing a Function
# John Kowal  -  WALTER$

import math

def calculate_total():
    meal = eval(input("Enter cost of your meal:  "))
    tax_rate = eval(input("Enter the percent tax:  "))
    tip_rate = eval(input("Enter the percent tip:  "))
    total = (meal + (meal * tax_rate / 100) + (meal * tip_rate / 100))
    print()
    print("The total cost of your meal is $",total)

calculate_total()
