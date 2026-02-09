y, k, n = map(int, input().split())

start = (y + 1 + k - 1) // k * k
max_s = (n // k) * k

if start > max_s:
    print(-1)
else:
    res = []
    current = start
    while current <= max_s:
        res.append(current - y)
        current += k
    print(' '.join(map(str, res)))