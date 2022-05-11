# Distinct powers
N = 100
print(len(set([i**j for i in range(2, N+1) for j in range(2, N+1)])))
