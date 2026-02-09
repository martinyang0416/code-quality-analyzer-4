import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    W = int(input[ptr])
    H = int(input[ptr+1])
    ptr += 2
    maze = []
    for _ in range(H):
        row = input[ptr]
        ptr += 1
        maze.append(row)
    
    score_table = []
    for _ in range(10):
        row = list(map(int, input[ptr:ptr+10]))
        ptr += 10
        score_table.append(row)
    
    start = None
    end = None
    items = {}
    for y in range(H):
        for x in ran