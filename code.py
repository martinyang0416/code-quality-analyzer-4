q = int(input())
for _ in range(q):
    h, w = map(int, input().split())
    rows = []
    for _ in range(h):
        row = list(map(int, input().split()))
        rows.append(row)
    is_mirrored = True
    for row in rows:
        if row != row[::-1]:
            is_mirrored = False
            break
    print("YES" if is_mirrored else "NO")