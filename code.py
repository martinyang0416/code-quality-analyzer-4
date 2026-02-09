n, C, D = map(int, input().split())
points = [int(input()) for _ in range(n)]
points.sort()

if n == 0:
    print(0.0)
else:
    dp = [float('inf')] * n
    dp[0] = C  # Covering just the first point with r=0
    
    for i in range(1, n):
        for j in range(i + 1):
            left = points[j]
            right = points[i]
            r = (right - left) / 2
            cost = C + D * r
            if j == 0:
                prev_cost = 0
            else:
                prev_cost = dp[j - 