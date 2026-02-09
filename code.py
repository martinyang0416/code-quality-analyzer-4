from collections import deque

def rotate_right(s, N):
    return ((s >> 1) | ((s & 1) << (N - 1))) & ((1 << N) - 1)

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1
    for _ in range(T):
        L_str = input[idx]
        idx += 1
        S_str = input[idx]
        idx += 1
        L = int(L_str, 2)
        S = int(S_str, 2)
        target = L
        
        visited = {}
        q = deque()
