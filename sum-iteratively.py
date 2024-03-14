# Summing Numbers Iteratively
# John Kowal  -  WALTER$

n = 6

def sum(n):
    total = 0
    for i in range (1, n + 1):
        total += i
    return total

print(sum(n))
