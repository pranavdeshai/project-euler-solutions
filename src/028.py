# Number spiral diagonals
N = 1001
n = N*N
total = n
for i in range(N-1, 0, -2):
    for j in range(4):
        n = n - i
        total += n
print(total)
