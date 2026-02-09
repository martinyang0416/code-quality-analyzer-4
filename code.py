import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        W = list(map(int, data[idx:idx+N]))
        idx += N
        max_val = max(W)
        s = N // 2
        max_positions = [i for i in range(N) if W[i] == max_val]
        intervals = []
        for m in max_positions:
            a = (N - m) % N
            end = a + s - 1
            if end < N:
  