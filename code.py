n, a, b = map(int, input().split())
new_index = (a - 1 + b) % n
print(new_index + 1)