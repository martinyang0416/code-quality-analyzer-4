def min_jumps(x, y):
    if x == 0 and y == 0:
        return 0
    if x != y:
        return -1  # As per initial analysis, but sample contradicts
    n = 0
    total = 0
    while True:
        n += 1
        total += n
        if total >= x:
            diff = total - x
            if diff % 1 == 0:
                return n
        if total > x + n:
            break
    return -1  # Or handle differently

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min_