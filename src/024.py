# Lexicographic permutations
from itertools import permutations

p = list(permutations([i for i in range(10)]))
print(p[10**6 - 1])