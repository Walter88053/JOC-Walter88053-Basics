# Strings, Lists & Whiles
# John Kowal  -  WALTER$

import math

def average_neg_evens(list1):
    sum = 0
    count = 0
    neg_count = 0
    while count < len(list1):
        if list1[count] < 0  and list1[count] % 2 == 0:
            sum += list1[count]
            neg_count += 1
        count += 1
    return sum / neg_count

print()

def count_letter(list2, letter):
    count = 0
    letter = letter.lower()
    i = 0
    while i < len(list2):
        count += list2[i].lower().count(letter)
        i += 1
    return count

def main():
    list1 = [0, 1, 2, -2, -3, -4, 3, 4]
    print("The average of the negative numbers in the list is:  ", average_neg_evens(list1))
    list2 = ["HELLO", "goodbye", "1234 Oooh!"]
    print()
    print("The number of times that the specified letter appears in the list is:  ", count_letter(list2, "O"))

main()