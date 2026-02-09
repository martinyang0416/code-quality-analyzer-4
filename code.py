n = int(input())
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West

while n != -1:
    steps = 2 * n
    x, y = 0, 0
    for j in range(steps):
        dir_idx = j % 4
        dx, dy = directions[dir_idx]
        x += dx
        y += dy
    print(x)
    print(y)
    n = int(input())