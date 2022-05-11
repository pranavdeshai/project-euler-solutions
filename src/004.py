# Largest palindrome product
N = 999


def largest_product(n):
    visited = set()
    result = 0
    for i in range(N, 100, -1):
        for j in range(N, 100, -1):
            product = i * j
            if product not in visited:
                visited.add(product)
                if str(product) == str(product)[::-1]:
                    if product > result:
                        result = product
    return result


print(largest_product(N))
