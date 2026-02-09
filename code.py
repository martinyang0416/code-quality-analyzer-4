n = int(input())
arr = list(map(int, input().split()))
sum_total = sum(arr)
arr_sorted = sorted(arr, key=lambda x: abs(x))

contributions = []
for x in arr_sorted:
    if x < 0:
        contributions.append(2 * (-x))
    else:
        contributions.append(-2 * x)
contributions.sort(reverse=True)

prefix = [0] * (2 * n + 1)
for i in range(1, 2 * n + 1):
    if i-1 < len(contributions):
        prefix[i] = prefix[i-1] + contributions[i-1]
    else:
        prefix[i] = prefix[i-1]

max_sum = -float