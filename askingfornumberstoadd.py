# Activity: Asking for numbers to get a total
# John Kowal  -  WALTER$

def main():
    PROMPT = "Enter the next number to input for adding to get a total or 0 when finished: "

    total = 0
    ele = 0
    list = []

    response = eval(input(PROMPT))
    while response != 0:
        list.append(response)
        response = eval(input(PROMPT))
        total = total + list[ele]
        ele += 1

    print("The total of the inputted numbers is", total)

main()