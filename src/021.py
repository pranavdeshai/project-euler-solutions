# Amicable numbers
def get_factors(n):
    s1, s2 = [], []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            s1.append(i)
            s2.append(n//i)
    if s1[-1] != s2[-1]:
        return s1 + s2[::-1]
    return s1[:-1] + s2[::-1]


def d(n):
    if n == 1:
        return 1
    x = get_factors(n)
    x.pop()
    return sum(x)


amicable_numbers = []
for i in range(1, 10000):
    j = d(i)
    if j not in amicable_numbers:
        if i != j:
            if d(j) == i:
                amicable_numbers.append((d(i)))
print(amicable_numbers, sum(amicable_numbers))
