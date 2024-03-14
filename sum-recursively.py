# Summing Numbers Recursively
# John Kowal  -  WALTER$

n = 6

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

print(sum(n))
