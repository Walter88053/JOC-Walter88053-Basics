# Lists & Strings - Counting vowels in a list of Strings
# John Kowal  -  WALTER$

# Second Try

# list = ["hi", "hello", "OOF!"]

def count_vowels(list):
    num_v = 0
    for string in list:
        for v in "AEIOU":
            num_v += string.upper().count(v)
    return num_v

print(count_vowels(["hi", "hello", "OOF!"]))
print("count_vowels", count_vowels(["hi", "hello", "OOF!"]) == 5)

# NOTE:  On line 12, the user must enter an upper case letter for counting both cases.
#        Also, on line 12, entering a lower case letter will output "0".
#        On lines 16 & 17, the user must enter the contents of the list that is to be searched.