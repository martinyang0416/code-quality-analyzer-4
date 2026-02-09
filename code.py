import math

n = int(input())
a = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    start = l - 1
    end = r - 1
    count = 0
    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):
            if math.gcd(a[i], a[j]) > 1:
                count += 1
    print(count)