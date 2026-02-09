n = int(input())
a = list(map(int, input().split()))
from collections import defaultdict

counts = defaultdict(int)
for num in a:
    bits = bin(num).count('1')
    counts[bits] += 1

result = 0
for c in counts.values():
    result += c * (c - 1) // 2

print(result)