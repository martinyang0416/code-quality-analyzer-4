from collections import deque

def maxDistance(grid):
    n = len(grid)
    if n == 0:
        return -1
    
    count_ones = sum(row.count(1) for row in grid)
    if count_ones == 0 or count_ones == n * n:
        return -1
    
    distance = [[-1] * n for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                distance[i][j] = 0
                queue.append((i, j))
    
    directions = [(-1, 0), (1, 0), (0, -1