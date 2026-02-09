import sys
import bisect
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    cows = []
    for i in range(N):
        if s[i] == '1':
            cows.append(i+1)
    total_C = len(cows)
    if total_C == 0:
        return

    # 