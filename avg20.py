# Calculate average of 20 numbers inputted by the user
# John Kowal  -  WALTER$

# numbers = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

print()
numbers = []
for i in range(20):
    numbers.append(eval(input("Please enter 1 of 20 numbers: ")))

print()
print(numbers)
for i in range(1):
    print("The average is: ", sum(numbers) / 20)
