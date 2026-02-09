MOD = 1000009

def main():
    import sys
    h, w, p = map(int, sys.stdin.readline().split())
    is_penalty = [[False]*(w+1) for _ in range(h+1)]
    for _ in range(p):
        row, col = map(int, sys.stdin.readline().split())
        is_penalty[row][col] = True
    
    # Initialize DP table
    dp = [[[0]*(p+1) for _ in range(w+1)] for __ in range(h+1)]
    
    # Starting cell (1,1)
    if is_penalty[1][1]:
        dp[1][1][1] = 1
    else:
        dp[1][1][0] = 1
    
    for i in range(1,