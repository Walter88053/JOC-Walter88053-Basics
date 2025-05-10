x, y = 15, 91  # define range [x, y]

res = []  # list to store primes

for n in range(x, y + 1):
    if n <= 1:
        continue  # skip non-primes <= 1

    is_prime = True  # assume n is prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False  # n is not prime
            break

    if is_prime:
        res.append(n)  # add prime number

print()
print("The primes numbers between", x, "and", y, "are")
print(res if res else "No")


