import sys
from collections import deque

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, a, b = map(int, sys.stdin.readline().split())
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)
        
        # Calculate component size containing b when a is removed
        visited = [False] * (n + 1)
        q = deque([b])
        visit