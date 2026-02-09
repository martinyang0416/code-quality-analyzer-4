def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx +=2
        A = list(map(int, input[idx:idx+N]))
        idx +=N
        total = sum(A)
        max_k = sum(A[:K])
        current = max_k
        for i in range(K, N):
            current += A[i] - A[i-K]
            if current > max_k:
                max_k = current
        window_nk = N - K
      