n, m = map(int, input().split())
a = list(map(int, input().split()))
from collections import Counter
counts = Counter(a)
total = n * (n - 1) // 2
same = sum(c * (c - 1) // 2 for c in counts.values())
print(total - same)