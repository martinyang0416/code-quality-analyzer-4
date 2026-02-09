from collections import deque

def read_grid():
    grid = []
    for _ in range(3):
        row = list(map(str, input().split()))
        grid.extend(row)
    return ''.join(grid)

def main():
    target = "123456780"
    while True:
        line = input()
        if line == '-1':
            break
        # Read the next two lines
        grid_part = [line.strip()]
        grid_part.append(input().strip())
        grid_part.append(input().strip())
        # Process each test case
        initi