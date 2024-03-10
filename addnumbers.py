# Activity: Adding 2 numbers
# John Kowal  -  WALTER$

def addNumbers(a, b):
    sum = a + b
    return sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = addNumbers(num1, num2)
print("The sum is", result)
