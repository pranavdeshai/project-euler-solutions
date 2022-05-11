# Summation of primes
def is_prime(n):
    "Returns True if the given number is prime, False otherwise."
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


N = 2 * 10**6


def solve(N):
    total = 0
    for i in range(N):
        if is_prime(i):
            total += i
    return total


print(solve(N))
