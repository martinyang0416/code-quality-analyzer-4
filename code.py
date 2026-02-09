t = int(input())
for _ in range(t):
    s = input().strip()
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    total = sum(min(2, count) for count in freq.values())
    k = total // 2
    print(k)