# Writing While Loops
# John Kowal  -  WALTER$

j = 1
while j < 6:
    print(j)
    j += 1

print()

k = 2
while k < 12:
    print(k)
    k += 3

print()

l = -10
while l < 1:
    print(l,"", end="",)
    l += 2
print()
print()

i = 0
while i < 4:
    print("****")
    i += 1

print()

string = "CSCI 150"
builder = ""
m = 0
while m < len(string):
    builder = string[m]
    print(builder)
    m += 1

print()

list = []
prompt = "Please enter a list of numbers  (1 at a time, then '0' to end)"
response = eval(input(prompt))
while response != 0:
    list.append(response)
    response = eval(input(prompt))
print(sorted(list))
print(sum(list))
print(sum(list) / len(list))
