# Printing 3 Pyramids by Writing a Function
# John Kowal  -  WALTER$

r = 2
s = 5
t = 10

def past(text, r):
    length = len(text) + 1
    for length in range(1, r + 1, 1):
        print(text * length)

def plus(text, s):
    length = len(text) + 1
    for length in range(1, s + 1, 1):
        print(text * length)

def px(text, t):
    length = len(text) + 1
    for length in range(1, t + 1, 1):
        print(text * length)

def main():
    past("*", r)
    print()
    plus("+", s)
    print()
    px("x", t)
    print()

main()
