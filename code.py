T = int(input())
for _ in range(T):
    s = input().strip()
    total = 0
    for c in s:
        total += ord(c.lower()) - ord(c)
    print(total)