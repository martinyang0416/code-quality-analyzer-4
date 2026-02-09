import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, c = map(int, sys.stdin.readline().split())
        adj[u].append((v, c))
        adj[v].append((u, c))
    
    # BFS to find spanning tree
    parent = [0] * (N + 1)
    edge_c = [0] * (N + 1)
    visited = [False] * (N + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    parent[1] = 0
    edge_c[1] = 0  # dummy