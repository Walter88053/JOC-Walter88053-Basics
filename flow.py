# Reading Ifs & Flowing Functions
# John Kowal  -  WALTER$

x = 29

def f(x):
    x = x-1
    return g(x)+1

def g(x):
    return x*2

def h(x):
    if x%2 == 1:
        return f(x) + x
    else:
        return f(f(x))

print(h(3))
print(h(4))
print(h(5))