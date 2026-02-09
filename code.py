import sys
from collections import defaultdict

n, p = map(int, sys.stdin.readline().split())
count = [0] * (n + 1)  # 1-based indexing
pair_count = defaultdict(int)

for _ in range(n):
    xi, yi = map(int, sys.stdin.readline().split())
    a, b = sorted((xi, yi))
    count[a] += 1
    count[b] += 1
    pair_count[(a, b)] += 1

counts_sorted = sorted(count[1:n+1])
total = 0
length = len(counts_sorted)

for i in range(length):
    left = i + 1
    right = length - 1
    j = length  # Initialize 