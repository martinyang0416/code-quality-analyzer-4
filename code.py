n, m = map(int, input().split())
x = int(input())
count = 0

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            continue
        a = i
        b = j
        c = (n - 1) - i
        d = (m - 1) - j
        t = min(a, b, c, d)
        if t + 1 == x:
            count += 1

print(count)