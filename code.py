import math

t = int(input())
for case in range(1, t + 1):
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    denominator = math.hypot(dx, dy)
    q = int(input())
    print(f"Test case : {case}")
    for _ in range(q):
        x3, y3 = map(int, input().split())
        cross = dx * (y3 - y1) - dy * (x3 - x1)
        if cross == 0:
            print("YES")
        else:
            distance = abs(cross) / denominator
            print("NO")
            print("{0