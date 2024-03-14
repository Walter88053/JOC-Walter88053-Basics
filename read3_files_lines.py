# Read 3 text files and then output the number of lines in each file
# John Kowal  -  WALTER$

open("counts.txt", "w").close()
def countline(textx):
    file = open(textx + ".txt", 'r')
    count = 0
    list = file.read()
    linelist = list.split("\n")
    for i in linelist:
        if i:
            count += 1
    file.close()

    count_file = open("counts.txt", 'a')
    count_file_text = textx + ".txt : " + str(count) + "\n"
    count_file.write(count_file_text)
    print(count_file_text, end ="")
    count_file.close()

def main():
    for x in range(0, 3):
        textx = "text" + str(x+1)
        countline(textx)

main()