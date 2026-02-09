p, m, x = map(int, input().split())
total = p * x * (x + 1) // 2
borrow = max(0, total - m)
print(borrow)