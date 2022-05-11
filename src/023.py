# Non-abundant sums
def get_factors(n, proper=False):
    factors = []
    for i in range(1, int(n**(1/2))):
        if n % i == 0:
            factors.append(i)
    if n**0.5 * n**0.5 == float(n):
        factors.append(int(n**0.5))
    factors += [n//i for i in factors[::-1]]
    return factors[:-1] if proper else factors


abnums = [i for i in range(1, 28124) if sum(get_factors(i, proper=True)) > i]
# x = [i + j for i in abnums for j in abnums]
print(abnums)
