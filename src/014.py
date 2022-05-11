# Longest Collatz sequence
longest_chain = 0
for i in range(1, 10**6):
    chain = 1
    n = i
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = 3*i + 1
        chain += 1
    if chain > longest_chain:
        longest_chain = chain
        result = n
print(result)
