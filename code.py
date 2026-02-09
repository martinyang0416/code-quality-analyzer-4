import sys
import heapq

def solve():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        islands = []
        sum_total = 0
        for _ in range(n):
            t, c = map(int, sys.stdin.readline().split())
            islands.append((t, c))
            sum_total += t
        
        possible = False
        for last_idx in range(n):
            last_t, last_c = islands[last_idx]
            if last_c < sum_total:
                continue
   