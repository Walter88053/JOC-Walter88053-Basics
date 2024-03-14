# Activity: Prints the contents of a text file
# John Kowal  -  WALTER$

read_file = open("greetings.txt")
for line in read_file:
    print("-", end="")
    print(line.rstrip())
read_file.close()

