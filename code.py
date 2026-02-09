import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_size = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j