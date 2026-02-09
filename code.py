from collections import Counter
import sys
import math

n = int(sys.stdin.readline())
elements = list(map(int, sys.stdin.readline().split()))
elements.sort(reverse=True)
freq = Counter(elements)

result = []
for num in elements:
    if freq[num] <= 0:
        continue
    result.append(num)
    freq[num] -= 1
    for y in result[:-1]:
        g = math.gcd(num, y)
        freq[g] -= 2
        if freq[g] == 0:
            del freq[g]
    if len(result) == n:
        break

print(' '.join(map(str, 