a = int(input())
b = int(input())
d = abs(a - b)
if d % 2 == 0:
    print(d * (d + 2) // 4)
else:
    print((d + 1) ** 2 // 4)