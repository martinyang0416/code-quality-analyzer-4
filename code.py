n, k = map(int, input().split())
events = []
for _ in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))
    events.append((r + 1, -1))

events.sort()

result = 0
current_coverage = 0
prev_x = None

MOD = 10**9 + 7

for x, delta in events:
    if prev_x is not None and x > prev_x:
        if current_coverage >= k:
            result += (x - prev_x)
    current_coverage += delta
    prev_x = x

print(result % MOD)