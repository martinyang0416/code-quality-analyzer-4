n = int(input())
d = list(map(int, input().split()))

min_max = float('inf')

for i in range(1, n - 1):
    new_d = d[:i] + d[i+1:]
    current_max = 0
    for j in range(len(new_d) - 1):
        diff = new_d[j+1] - new_d[j]
        if diff > current_max:
            current_max = diff
    if current_max < min_max:
        min_max = current_max

print(min_max)