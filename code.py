import math

n, px, py = map(int, input().split())
vertices = [tuple(map(int, input().split())) for _ in range(n)]

max_dist_sq = 0
min_dist_sq = float('inf')

for x, y in vertices:
    dx = x - px
    dy = y - py
    dist_sq = dx * dx + dy * dy
    max_dist_sq = max(max_dist_sq, dist_sq)
    min_dist_sq = min(min_dist_sq, dist_sq)

for i in range(n):
    a = vertices[i]
    b = vertices[(i + 1) % n]
    ax, ay = a
    bx, by = b
    abx = bx - ax
    aby = by - ay
    apx = px - ax
    apy = py