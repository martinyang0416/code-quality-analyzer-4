from collections import Counter

s = input().strip()
counts = Counter(s)
n = len(s)
max_count = max(counts.values())
if max_count > (n + 2) // 3:
    print("NO")
else:
    print("YES")