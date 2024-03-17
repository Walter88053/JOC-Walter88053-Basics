# Read 3 text files and then output the number of lines and words in each file
# John Kowal  -  WALTER$

open("countlw.txt", "w").close()
def countlineword(textx):
    filel = open(textx + ".txt", 'r')
    countl = 0
    listl = filel.read()
    linelist = listl.split("\n")
    for i in linelist:
        if i:
            countl += 1
    filel.close()

    filew = open(textx + ".txt", 'r')
    countw = 0
    listw = filew.read()
    wordlist = listw.split()
    for k in wordlist:
        if k:
            countw += 1
    filew.close()

    count_file = open("countlw.txt", 'a')
    count_file_text = textx + ".txt : " + str(countl) + " lines, " + str(countw) + " words" + "\n"
    count_file.write(count_file_text)
    print(count_file_text, end ="")
    count_file.close()
    return countl, countw

def main():
    totall = 0
    totalw = 0
    for x in range(0,3):
        textx = "text" + str(x+1)
        countl, countw = countlineword(textx)
        totall += countl
        totalw += countw
    count_file = open("countlw.txt", 'a')
    count_file.write("TOTAL: " + str(totall) + " lines, " + str(totalw) + " words")
    print("TOTAL: " + str(totall) + " lines, " + str(totalw) + " words")

main()
