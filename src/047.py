# Distinct prime factors
def prime_factors(n):
    res = set()
    while n % 2 == 0:
        res.add(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            res.add(i)
            n = n // i
    if n > 2:
        res.add(n)

    return res


N = 4
i = 2*3*5*7
while True:
    l1 = len(prime_factors(i))
    if l1 == N:
        l2 = len(prime_factors(i + 1))
        if l2 == N:
            l3 = len(prime_factors(i + 2))
            if l3 == N:
                l4 = len(prime_factors(i + 3))
                if l4 == N:
                    print(i)
                    break
    i += 1
