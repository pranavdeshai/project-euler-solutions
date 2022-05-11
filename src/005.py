# Smallest multiple
def isprime(n):
    """Returns True if the given number is prime, False otherwise.
    Trial division with 6k+-1 rule."""

    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    # i = 5
    # while i**2 <= n:
    #     if n % i == 0 or n % (i + 2) == 0:
    #         return False
    #     i += 6

    for i in range(5, int(n**0.5) + 2, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


# nums = list(range(1, 1000))
# primes = [i for i in range(max(nums)) if is_prime(i)]
# lcm = 1
# while not all([i == 1 for i in nums]):
#     for p in primes:
#         tmp = [n // p if n % p == 0 else n for n in nums]
#         if tmp != nums:
#             break
#     nums = tmp
#     lcm *= p
# print(lcm)
primes = [i for i in range(1000) if isprime(i)]
print(primes, len(primes))
