n, p = map(int, input().split())

def factorize(x):
    factors = {}
    i = 2
    while i * i <= x:
        while x % i == 0:
            factors[i] = factors.get(i, 0) + 1
            x = x // i
        i += 1
    if x > 1:
        factors[x] = 1
    return factors

factors = factorize(p)
result = 1
for prime, exp in factors.items():
    cnt = exp // n
    if cnt > 0:
        result *= prime ** cnt

print(result)