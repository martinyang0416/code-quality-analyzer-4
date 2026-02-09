import sys
from collections import deque

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    special = list(map(int, sys.stdin.readline().split()))
    special_set = set(special)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        if u != v:
            edges.append((w, u, v))
    edges.sort()

    parent = list(range(n+1))
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = 