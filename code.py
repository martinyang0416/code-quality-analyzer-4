t = int(input())
for _ in range(t):
    n = input().strip()
    summands = []
    length = len(n)
    for i in range(length):
        d = int(n[i])
        if d != 0:
            power = 10 ** (length - 1 - i)
            summand = d * power
            summands.append(summand)
    print(len(summands))
    if summands:
        print(' '.join(map(str, summands)))
    else:
        print()