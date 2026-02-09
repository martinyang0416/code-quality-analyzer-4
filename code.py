def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())

    # Initialize a 2D DP array. dp[j][i] means using j terms to get sum i.
    # We need a (M+1) x (N+1) array.
    dp = [[False] * (N + 1) for _ in range(M + 1)]
    dp[0][0] = True  # 0 terms sum to 0

    for j in range(1, M + 1):
        for i in range(N + 1):
            if dp[j-1][i]:
                # Try adding a square of s (s can be 0)
                max_s = int((N - i) ** 0.5)
                for s in range