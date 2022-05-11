# Special Pythagorean triplet
N = 1000


def solve(N):
    for i in range(1, N):
        for j in range(1, N):
            if i + j + (i**2 + j**2)**(1/2) == 1000:
                return (i * j * (1000 - (i + j)))


print(solve(N))
