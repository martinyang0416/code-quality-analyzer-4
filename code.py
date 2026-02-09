n, k = map(int, input().split())
a = list(map(int, input().split()))
min_hours = float('inf')
for ai in a:
    if ai <= k and k % ai == 0:
        current = k // ai
        if current < min_hours:
            min_hours = current
print(min_hours)