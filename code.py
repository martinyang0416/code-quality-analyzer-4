import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)
    
    cows = [i+1 for i in range(N) if s[i] == '1']
    T = len(cows)
    if T == 0:
        print("No solution")
        return
    
    # Compute all pairwis