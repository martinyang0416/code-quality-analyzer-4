while True:
    line = input().strip()
    if not line:
        continue
    H, W = map(int, line.split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        row = ''.join('#' if (i + j) % 2 == 0 else '.' for j in range(W))
        print(row)
    print()