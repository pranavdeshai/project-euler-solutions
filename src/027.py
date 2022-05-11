# 27. Quadratic primes
from itertools import count


def isprime(n):
    """Returns True if the given number is prime, False otherwise.
    Trial division with 6k+-1 rule."""

    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 2, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def quadprimes():
    maxstreak = 0
    x, y = 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            streak = 0
            for i in count():
                if isprime((i ^ 2) + (a * i) + b):
                    streak += 1
                else:
                    break
            if streak > maxstreak:
                maxstreak = streak
                x, y = a, b
    return x, y


quadprimes()
