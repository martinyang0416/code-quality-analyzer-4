import sys
from collections import deque

def main():
    H, W, K = map(int, sys.stdin.readline().split())
    grid = []
    start = None
    for i in range(H):
        row = sys.stdin.readline().strip()
        grid.append(list(row))
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
    
    # Precompute distance to the nearest exit for each cell
    distance = [[-1] * W for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in range(W)