n, d = map(int, input().split())
print(d + (n - d - 1) * (n + d) // 2)