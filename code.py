import sys
from sys import stdin
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n, m = map(int, stdin.readline().split())
    h = list(map(int, stdin.readline().split()))
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        in_degree[v] += 1

    # Compute topological order
    queue = deque()
    for i in range(n):
       