# Factoral digit sum
def fac(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p


print(sum([int(i) for i in str(fac(100))]))
