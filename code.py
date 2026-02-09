n = int(input())
d = list(map(int, input().split()))
t = int(input())

d.sort(reverse=True)
current_sum = 0
max_k = 0

for i in range(n):
    current_sum += d[i]
    if current_sum <= t:
        max_k = i + 1
    else:
        break  # No need to check further as sorted in descending order

print(max_k)