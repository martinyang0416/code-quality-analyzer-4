def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr +=1
    M = int(input[ptr])
    ptr +=1
    
    D = []
    for _ in range(N):
        D.append(int(input[ptr]))
        ptr +=1
    
    T = []
    for _ in range(M):
        T.append(int(input[ptr]))
        ptr +=1
    
    INF = float('inf')
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for j in range(1, M + 1):
        for i in range(N + 1):
            # 