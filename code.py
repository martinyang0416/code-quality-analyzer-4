n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total_a = sum(a)

# Determine minimal k using sorted b in descending order
sorted_b = sorted(b, reverse=True)
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + sorted_b[i]
k = next(i for i in range(1, n + 1) if prefix_sum[i] >= total_a)

# Dynamic programming to find maximum sum_a for subsets of size k with sum_b >= total_a
dp = [{} for _ in range(n + 1)]
dp[0][0] = 0

for