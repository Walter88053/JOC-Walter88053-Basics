# Read 3 text files and then output the number of lines and words in each file
# John Kowal  -  WALTER$

def countlineword(textx):
    with open(textx + ".txt", 'r') as filel:
        countl = 0
        listl = filel.read()
        linelist = listl.split("\n")
        for i in linelist:
            if i:
                countl += 1

    with open(textx + ".txt", 'r') as filew:
        countw = 0
        listw = filew.read()
        wordlist = listw.split()
        for j in wordlist:
            if j:
                countw += 1

    with open("countlw.txt", 'a') as count_file:
        count_file_text = textx + ".txt : " + str(countl) + " lines, " + str(countw) + " words" + "\n"
        count_file.write(count_file_text)
        print(count_file_text, end="")


def main():
    open("countlw.txt", "w").close()

    total_lines = 0
    total_words = 0

    for x in range(0, 3):
        textx = "text" + str(x + 1)
        countlineword(textx)

    with open("countlw.txt", 'r') as count_file:
        lines = [t for t in count_file]
        for line in lines:
            line_words = line.split(", ")
            total_lines += int(line_words[0].split()[2])
            total_words += int(line_words[1].split()[0])

        count_file = open("countlw.txt", 'a')
        count_file.write("TOTAL: " + str(total_lines) + " lines, " + str(total_words) + " words")
        print("TOTAL: " + str(total_lines) + " lines, " + str(total_words) + " words")

main()
