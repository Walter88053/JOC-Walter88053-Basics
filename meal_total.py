# Calculate Total Meal Cost by Writing a Function
# John Kowal  -  WALTER$

import math

def calculate_total(meal, tax_rate, tip_rate):
    total = (meal + (meal * tax_rate) + (meal * tip_rate))
    print()
    print("The total cost of your meal is $", total)

calculate_total(53.48, .07, .18)
