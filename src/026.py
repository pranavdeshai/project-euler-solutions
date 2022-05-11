# Reciprocal cycles
from matplotlib import pyplot as plt
import sys


def rec_cycles(den, num=1):
    while num < den:
        num *= 10
    q = [num // den]  # List of quotients
    r = [num % den]  # List of remainders
    while not r[-1] in [0, num] + r[:-1]:
        q.append(r[-1] * 10 // den)
        r.append(r[-1] * 10 % den)
    return len(q) - 1


N = int(sys.argv[1]) + 1
print(max([i for i in range(1, N)], key=rec_cycles))
plt.plot([i for i in range(1, N)], [rec_cycles(i) for i in range(1, N)])
plt.show()
