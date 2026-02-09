import sys
from collections import defaultdict, deque

sys.setrecursionlimit(1 << 25)

def main():
    n = int(sys.stdin.readline())
    if n % 2 != 0:
        print(0)
        return

    edges = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    parent = [0]*(n+1)
    children = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    q = deque([1])
    visited[1] = True
    while q: