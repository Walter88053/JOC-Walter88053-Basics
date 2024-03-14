# Sorting grades from a txt file and calculating the median
# John Kowal  -  WALTER$

file = open("gradesort.txt", "r")

import statistics
def gradesort():
    gradefile = open("gradesort.txt", "r")
    column = []
    for line in gradefile:
        field = line.split(",")
        grade = int(field[2])
        column.append(grade)

    column.sort()
    gradefield = column
    print(gradefield)

    grademedian = statistics.median(gradefield)
    print("Median of grades is " + str(grademedian))

    gradefile.close()

gradesort()