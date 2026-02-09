def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    
    # Initialize DP table where dp[i][j] indicates if sum i can be formed with j squares
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True  # Base case: 0 sum with 0 squares
    
    for i in range(N + 1):
        for j in range(1, M + 1):
            max_k = int(i ** 0.5)  # Maximum possible integer k such that k^2 <= i
            for k in range(0, max_k + 1):
                square = k * k
 