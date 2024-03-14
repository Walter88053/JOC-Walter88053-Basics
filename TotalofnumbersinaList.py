# Finding the total of numbers in a list
# John Kowal  -  WALTER$

def totalNumbers(list):
    total = 0
    ele = 0
    list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    while ele < len(list1):
        total = total + list1[ele]
        ele += 1
    print("The total of the listed numbers is", total)

totalNumbers(list)