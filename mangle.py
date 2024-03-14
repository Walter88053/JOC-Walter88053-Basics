# Lists & Strings - Adding & Omitting Characters From a String
# John Kowal  -  WALTER$

def mangle(text):
    text = text.upper()
    text = text[0:2] + text[3:-3] + text[-2:]
    return text

print()
print(mangle("hellothere"))
print(mangle("42 degrees Celsius"))
print(mangle("eeeeeee"))

