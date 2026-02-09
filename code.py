import math

n = int(input())
sum_a = 0
for _ in range(n):
    a, g = map(int, input().split())
    sum_a += a

lower_k = max(0, math.ceil((sum_a - 500) / 1000))
upper_k = min(n, math.floor((sum_a + 500) / 1000))

if lower_k > upper_k:
    print(-1)
else:
    k = lower_k
    print('G' * k + 'A' * (n - k))