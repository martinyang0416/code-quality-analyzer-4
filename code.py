import sys
from math import gcd
from functools import lru_cache

@lru_cache(maxsize=None)
def compute_steps(a, b):
    if a == 0 or b == 0:
        return 0
    d = gcd(a - 1, b - 1)
    new_a = (a - 1) // d
    new_b = (b - 1) // d
    return 1 + compute_steps(new_a, new_b)

T = int(sys.stdin.readline())
for _ in range(T):
    parts = sys.stdin.readline().strip().split()
    x = int(parts[0])
    y = int(parts[1])
    starter = parts[2]
    
    g = gcd(x, y)
    a = x // g
    b = y // g
    
