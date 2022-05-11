# 1000 digit Fibonacci number
def fib(n):
    if n in [1, 2]:
        return 1
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


x = 1
while len(str(fib(x))) < 1000:
    x += 1

print(x, fib(x))
