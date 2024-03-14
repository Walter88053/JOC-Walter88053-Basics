# Calculate average of 10 real numbers using a for loop
# John Kowal  -  WALTER$

s = 0
for i in range(10):
    rn = float(input("Enter a real number: "))
    s += rn
print ("The average is: ", s / 10)