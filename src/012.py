# Highly divisible triangular number
def is_prime(n):
    "Returns True if the number is prime using 6k+-1 primality test"
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**(1/2)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def get_factors(n):
    """Returns the improper factors of the given number"""
    factors = []
    for i in range(1, int(n**(1/2))):
        if n % i == 0:
            factors.append(i)
    if n**0.5 * n**0.5 == float(n):
        factors.append(int(n**0.5))
    factors += [n//i for i in factors[::-1]]
    return factors


i = 1
while True:
    n = (i * (i + 1)) // 2
    l = len(get_factors(n))
    if l > 500:
        print(n)
        break
    i += 1
