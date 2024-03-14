# Lists & Strings - Counting vowels in a list of Strings
# John Kowal  -  WALTER$

# First Try

# list = ["hi", "hello", "OOF!"]

def count_vowels(v):
    num_v = 0
    for string in v:
        num_v += string.upper().count("A")
        num_v += string.upper().count("E")
        num_v += string.upper().count("I")
        num_v += string.upper().count("O")
        num_v += string.upper().count("U")
    return num_v

print(count_vowels(["hi", "hello", "OOF!"]))
print("count_vowels", count_vowels(["hi", "hello", "OOF!"]) == 7)

# NOTE:  On line 13 thru 18, the user must enter an upper case letter for counting both cases.
#        Also, on those lines, entering a lower case letter will output "0".
#        On lines 20 & 21, the user must enter the contents of the list that is to be searched.