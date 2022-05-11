# Lattice paths
def fac(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


N = 20
print(fac(2*N) // (fac(N) * fac(N)))
