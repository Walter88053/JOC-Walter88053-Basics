# Lists & Strings - Counting "E"'s and "e"'s in a String
# John Kowal  -  WALTER$

# list = ["hi", "hello", "EEK!"]

def count_e(list):
    num_e = 0
    for string in list:
        num_e += string.upper().count("E")
    return num_e

print(count_e(["hi", "hello", "EEK!"]))
print("count_e", count_e(["hi", "hello", "EEK!"]) == 5)

# NOTE:  On line 11, the user must enter an upper case letter for counting both cases.
#        Also, on line 11, entering a lower case letter will output "0".
#        On lines 14 & 15, the user must enter the contents of the list that is to be searched.