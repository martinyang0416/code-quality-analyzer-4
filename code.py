from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(int)
count = 0

for num in arr:
    r = num % k
    complement = (k - r) % k
    count += freq[complement]
    freq[r] += 1

print(count)