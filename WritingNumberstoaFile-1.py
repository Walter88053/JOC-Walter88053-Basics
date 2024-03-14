# Writing Numbers to a File #1
# John Kowal  -  WALTER$

def main():

    PROMPT = "Enter the next number to input to the file or 0 when finished: "

    outfilename = input("What is the name of the output file? ")
    numLines = eval(input("How many numbers do you want to write to the file? "))

    dataFile = open(outfilename+".txt", "w")
    for x in range(numLines):
        userinput = input(PROMPT)
        print(userinput, file=dataFile)
    dataFile.close()
    dataFile = open(outfilename+".txt")
    lines = dataFile.readlines()
    for line in lines:
        print()

main()