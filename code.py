def get_factors(n):
    counts = {2:0, 3:0, 5:0}
    for prime in [2, 3, 5]:
        while n % prime == 0:
            counts[prime] += 1
            n = n // prime
    return counts[2], counts[3], counts[5], n

a, b = map(int, input().split())

a2, a3, a5, a_rest = get_factors(a)
b2, b3, b5, b_rest = get_factors(b)

if a_rest != b_rest:
    print(-1)
else:
    print(abs(a2 - b2) + abs(a3 - b3) + abs(a5 - b5))