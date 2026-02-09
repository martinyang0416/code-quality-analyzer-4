m, x, y = map(int, input().split())
z = ((x + y - 1) % m) + 1
print(z)