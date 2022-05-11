# 10001st prime
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


N = 10001
i = 1
n = 0
while N > n:
    if is_prime(i):
        n += 1
        print(i)
    i += 1
print(i - 1)
