import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    for _ in range(T):
        light_str = input[idx]
        switch_str = input[idx+1]
        idx += 2

        # Convert to bitmasks
        L0 = 0
        S0 = 0
        for i in range(N):
            L0 <<= 1
            L0 += int(light_str[i])
            S0 <<= 1
            S0 += int(switch_str[i])

        # Pre