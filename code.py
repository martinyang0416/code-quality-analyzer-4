import bisect
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for _ in range(T):
        S = input[ptr]
        ptr +=1
        Q = int(input[ptr])
        ptr +=1
        Ts = list(map(int, input[ptr:ptr+Q]))
        ptr += Q
        
        n = len(S)
        prefix = [0] * (n + 1)
        for i in range(1, n+1):
            if S[i-1] == 'a':
                prefix[i] = prefix[i-1] + 1
   