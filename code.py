a = int(input())
perm = [4, 1, 3, 2, 0, 5]
result = 0
for i in range(6):
    if a & (1 << i):
        result += 1 << perm[i]
print(result)