import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    a = list(map(int, input[idx:idx+N]))
    idx += N
    Q = int(input[idx])
    idx += 1
    queries = []
    for _ in range(Q):
        i = int(input[idx])
        j = int(input[idx+1])
        queries.append((i-1, j))  # Convert to 0-based
        idx += 2

    S = sorted(a)
    P = [0] * (N + 1)
    for i in range(N):
        P[i + 1] = P[i] + S[i]
    T = 0
    fo