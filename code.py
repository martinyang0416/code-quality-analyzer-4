from math import gcd
from functools import lru_cache

def tilingRectangle(n: int, m: int) -> int:
    g = gcd(n, m)
    a, b = n // g, m // g
    if a > b:
        a, b = b, a

    @lru_cache(maxsize=None)
    def dfs(a, b):
        if a == b:
            return 1
        if a == 0 or b == 0:
            return 0
        if a > b:
            a, b = b, a
        if b % a == 0:
            return b // a
        res = a * b  # Upper bound with 1x1 squares
        for s in range(1, a + 1):
        