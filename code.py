def numDistinct(s: str, t: str) -> int:
    n, m = len(s), len(t)
    dp = [0] * (m + 1)
    dp[0] = 1
    for char in s:
        for j in range(m, 0, -1):
            if char == t[j-1]:
                dp[j] += dp[j-1]
    return dp[m]