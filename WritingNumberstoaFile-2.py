# Writing Numbers to a File #2
# John Kowal  -  WALTER$

def main():

    PROMPT = "Enter the next number to input to the file or 0 when finished: "

    outfilename = input("What is the name of the output file? ")

    list = []

    dataFile = open(outfilename+".txt", "w")
    response = eval(input(PROMPT))
    while response != 0:
        list.append(response)
        dataFile.write(str(response)+ "\n")
        response = eval(input(PROMPT))
    dataFile.close()
    dataFile = open(outfilename+ ".txt", "r")
    lines = dataFile.readlines()

    for line in lines:
        print(line, end="")

main()