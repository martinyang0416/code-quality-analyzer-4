import bisect
from collections import deque

x0, y0, x1, y1 = map(int, input().split())
n = int(input())

allowed_rows = {}
for _ in range(n):
    ri, ai, bi = map(int, input().split())
    if ri not in allowed_rows:
        allowed_rows[ri] = []
    allowed_rows[ri].append((ai, bi))

allowed_rows_processed = {}
for r in allowed_rows:
    intervals = allowed_rows[r]
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        a, b = interval
        if not merged