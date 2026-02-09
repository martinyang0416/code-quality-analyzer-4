import sys

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    cow = [False] * (n + 1)
    for i in range(n):
        if s[i] == '1':
            cow[i + 1] = True
    M = sum(cow)
    if M == 0:
        return

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    # Compute count f