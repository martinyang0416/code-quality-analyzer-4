n = int(input())
if n < 2:
    print(0)
else:
    result = (n - 1) * (n - 2) // 2
    print(result)