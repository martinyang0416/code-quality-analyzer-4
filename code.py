MOD = 10**9 + 7

n, m = map(int, input().split())
broken = set()
for _ in range(m):
    a = int(input())
    broken.add(a)

dp = [0] * (n + 1)
dp[0] = 1  # Starting point

for i in range(1, n + 1):
    if i in broken:
        dp[i] = 0
    else:
        dp[i] = dp[i-1]  # Add ways from previous step
        if i >= 2:
            dp[i] += dp[i-2]  # Add ways from two steps back
        dp[i] %= MOD  # Apply modulo to prevent overflow

print(dp[n] % MOD)