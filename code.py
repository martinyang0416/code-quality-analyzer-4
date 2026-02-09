def longestArithSeqLength(A):
    n = len(A)
    if n <= 2:
        return n
    dp = [{} for _ in range(n)]
    max_len = 2
    for j in range(n):
        for i in range(j):
            d = A[j] - A[i]
            prev = dp[i].get(d, 1)
            current = prev + 1
            dp[j][d] = max(current, dp[j].get(d, 0))
            if dp[j][d] > max_len:
                max_len = dp[j][d]
    return max_len