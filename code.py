n = int(input())
a = list(map(int, input().split()))

inversion_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inversion_count += 1

current_parity = inversion_count % 2

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    length = r - l + 1
    swaps = length // 2
    if swaps % 2 == 1:
        current_parity ^= 1
    print("even" if current_parity == 0 else "odd")