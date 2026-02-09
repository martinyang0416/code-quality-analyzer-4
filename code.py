MOD = 10**9 + 7

n, T = map(int, input().split())
movies = [tuple(map(int, input().split())) for _ in range(n)]

max_mask = 1 << n
# Initialize DP table with all zeros
dp = [[[0] * (T + 1) for _ in range(5)] for _ in range(max_mask)]

for i in range(n):
    t_i, c_i = movies[i]
    if t_i <= T:
        mask = 1 << i
        dp[mask][c_i][t_i] += 1

for mask in range(max_mask):
    for last in range(1, 5):
        for time in range(T + 1):
            if dp[mask][last][time] == 0:
               