import sys
from collections import defaultdict

MOD = 10**9 + 7

def main():
    N, M = map(int, sys.stdin.readline().split())
    strings = [sys.stdin.readline().strip() for _ in range(M)]

    groups = defaultdict(int)
    for j in range(N):
        key = tuple(s[j] for s in strings)
        groups[key] += 1

    max_m = N
    s = [0] * (max_m + 1)
    s[0] = 1
    for m in range(1, max_m + 1):
        s[m] = (m * s[m-1] + 1) % MOD

    product = 1
    for cnt in groups.values():
        produ