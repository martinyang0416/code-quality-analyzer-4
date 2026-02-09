t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    total = a + b
    sum_limit = total // 3
    min_ab = min(a, b)
    print(min(sum_limit, min_ab))