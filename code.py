import sys
import heapq

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        c, r, d, s = map(int, sys.stdin.readline().split())
        adj[c].append((d, r, s))
    a = list(map(int, sys.stdin.readline().split()))
    a = [0] + a  # a[1] to a[N] are the values

    INF = float('inf')
    arrival = [INF] * (N + 1)
    arrival[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    