a1, a2, n = map(int, input().split())
if n == 1:
    print(a2)
else:
    prev_prev = a1
    prev = a2
    for _ in range(2, n + 1):
        current = prev_prev + prev
        prev_prev, prev = prev, current
    print(current)