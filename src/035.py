# Circular primes
def is_prime(n):
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


N = 10**6
visited = set()
circular_primes = set()
for n in range(N+1):
    if is_prime(n) and not n in visited:
        num = str(n)
        if len(num) > 1:
            rotations = []
            for i in num:
                num = num[1:] + num[0]
                visited.add(int(num))
                rotations.append(int(num))
            if all(is_prime(x) for x in rotations):
                for x in rotations:
                    circular_primes.add(x)
        else:
            circular_primes.add(n)
print(len(circular_primes))
