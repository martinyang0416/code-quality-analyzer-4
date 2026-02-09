MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

max_mask = 1 << 20
cnt = [0] * max_mask

for num in a:
    cnt[num] += 1

for bit in range(20):
    for mask in range(max_mask):
        if not (mask & (1 << bit)):
            cnt[mask] += cnt[mask | (1 << bit)]

sum_terms = 0
for mask in range(1, max_mask):
    bits = bin(mask).count('1')
    f_t = cnt[mask]
    if f_t == 0:
        continue
    term = pow(2, f_t, MOD) - 1
    if bits % 2 == 1:
        term = -term
    sum_