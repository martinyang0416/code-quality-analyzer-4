n, b = map(int, input().split())
v = int(input())
max_h = 0.0

for _ in range(n):
    x, h = map(int, input().split())
    if v < x < b:
        numerator = h * (b - v)
        denominator = x - v
        H = numerator / denominator
        if H > max_h:
            max_h = H

print("{0:.6f}".format(max_h))