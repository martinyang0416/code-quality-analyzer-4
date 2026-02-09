P = int(input())
N = int(input())
B = list(map(int, input().split()))
K = int(input())

# Initialize dp array where dp[s] represents the maximum product for sum s
# We only need sums up to K
max_possible_sum = K
dp = [0] * (max_possible_sum + 1)
dp[0] = 1  # Base case: empty subset

for x in B:
    # Iterate from high to low to avoid using the same element multiple times
    for s in range(max_possible_sum, x - 1, -1):
        if dp[s - x] != 0:
            current_product = dp[s - x] * x
      