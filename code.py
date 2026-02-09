MOD = 10**9 + 7

y, m = map(int, input().split())

if y == 0:
    print(0)
else:
    a = (2 * y - 1) % MOD
    pow2m = pow(2, m, MOD)
    res = (a * pow2m + 1) % MOD
    print(res)