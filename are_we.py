# Repeating Phrases
# John Kowal  -  WALTER$

def are_we(n, string):
    for i in range (n):
        print("Are we", string, "yet?", end=" ")
    print()

def main():
    print()
    print('are_we(2, "there")')
    are_we(2, "there")
    print()
    print('are_we(3, "50")')
    are_we(3, "50")
    print()
    print('are_we(1, "")')
    are_we(1, "")
    print()
    print('are_we(0, "hey!")')
    are_we(0, "hey!")

main()