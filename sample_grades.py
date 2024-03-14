# Read an Excel file with sample grades and output Mean, Median, and STD
# John Kowal  -  WALTER$

import statistics

def calcmean():
    file = open("sample_grades.csv", "r")
    sumFall = 0
    countFall = 0
    sumSpring = 0
    countSpring = 0

    for line in file:
        field = line.split(",")
        if field[1] == "Fall 2016":
            gradeFall = int(field[2])
            sumFall += gradeFall
            countFall += 1

        elif field[1] == "Spring 2016":
            gradeSpring = int(field[2])
            sumSpring += gradeSpring
            countSpring += 1

    if countFall > 0:
        meanFall = sumFall / countFall


    if countSpring > 0:
        meanSpring = sumSpring / countSpring

    print("          Fall 2016", "  Spring 2016")
    print("Mean:       ", (round(meanFall, 2)), "     ", (round(meanSpring, 2)))

    file.close()
calcmean()

def calcmedian():
    file = open("sample_grades.csv", "r")
    countFall = 0
    countSpring = 0
    medianFall = 0
    medianSpring = 0

    columnf = []
    columns = []

    for line in file:
        field = line.split(",")
        if field[1] == "Fall 2016":
            countFall += 1
            grade = int(field[2])
            columnf.append(grade)

        elif field[1] == "Spring 2016":
            countSpring += 1
            grade = int(field[2])
            columns.append(grade)

    columnf.sort()
    columns.sort()

    if countFall > 0:
        medianFall = statistics.median(columnf)

    if countSpring > 0:
        medianSpring = statistics.median(columns)

    print("Median:     " , round(medianFall, 2) , "      ", round(medianSpring, 2))

    file.close()
calcmedian()

def calcSTD():
    file = open("sample_grades.csv", "r")
    countFall = 0
    countSpring = 0

    columnf = []
    columns = []

    for line in file:
        field = line.split(",")
        if field[1] == "Fall 2016":
            countFall += 1
            grade = int(field[2])
            columnf.append(grade)

        elif field[1] == "Spring 2016":
            countSpring += 1
            grade = int(field[2])
            columns.append(grade)

    if countFall > 0:
        stdevFall = statistics.stdev(columnf)

    if countSpring > 0:
        stdevSpring = statistics.stdev(columns)

    print("STD:         ", (round(stdevFall, 2)), "     ", (round(stdevSpring, 2)))

    file.close()
calcSTD()
