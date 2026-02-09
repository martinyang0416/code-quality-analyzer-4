a, b, c, d = map(int, input().split())
total = a + b + c + d
if total % 2 != 0:
    print("NO")
else:
    target = total // 2
    arr = [a, b, c, d]
    found = False
    for mask in range(1, 1 << 4):
        s = 0
        for i in range(4):
            if mask & (1 << i):
                s += arr[i]
        if s == target:
            found = True
            break
    print("YES" if found else "NO")