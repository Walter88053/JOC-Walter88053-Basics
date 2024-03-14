# Writing Print Functions
# John Kowal  -  WALTER$

def header(text: object, surround: object) -> object:
    length = len(text) + 4
    print(surround * length)
    print(surround, text, surround)
    print(surround * length)

def main():
    header("Hello, World!", "*")
    header("Python Rocks", "!")
    header("Coders 4 EVER", "+")

main()