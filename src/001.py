# Multiples of 3 or 5
def sum_of_multiples(n, p):
    return n*(p//n)*((p//n) + 1) // 2

def solve(a, b, k):
    return sum_of_multiples(a, k) + sum_of_multiples(b, k) - sum_of_multiples(a*b, k)

print(solve(3, 5, 999))
