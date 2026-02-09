import sys
from math import gcd
from collections import Counter

def main():
    S = sys.stdin.readline().strip()
    Q = int(sys.stdin.readline())
    for _ in range(Q):
        l, r, t = map(int, sys.stdin.readline().split())
        # Convert to 0-based indices
        substring = S[l-1:r]  # because r is exclusive in Python's slice
        n = len(substring)
        if t == 0:
            print("No")
            continue
        if n == 0:
            print("Yes")
            continue
      