# Writing Functions
# John Kowal  -  WALTER$

print("Let's see what the sum and product is of your numbers!")
print()

def main():
    add()
    multiply()

x = eval(input("What is your first number? "))
y = eval(input("What is your second number? "))
print()
def add(x, y):
    print("Adding your numbers %d and %d" % (x,y ))
    return x+y;
sum = add(x, y)
print("x+y", "=", sum)
print()

def multiply(x, y):
    print("Multiplying your numbers %d and %d" % (x,y ))
    return x*y;
product = multiply(x, y)
print("x*y", "=", product)
print()