import sys
from sys import stdin
from collections import deque

def main():
    n, m, h = map(int, stdin.readline().split())
    u = list(map(int, stdin.readline().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        a -= 1
        b -= 1
        delta = (u[b] - u[a]) % h
        if delta == 1:
            adj[a].append(b)
        elif delta == h - 1:
            adj[b].append(a)
    
    # Kosaraju's algorithm to find SCCs
 