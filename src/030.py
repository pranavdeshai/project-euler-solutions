# Digit fifth powers
total = 0
powers = {i: i**5 for i in range(10)}
for n in range(2, 10**6 + 1):
    if sum(powers[int(i)] for i in str(n)) == n:
        total += n
print(total)
