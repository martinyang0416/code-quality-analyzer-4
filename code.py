import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + a[i]

    for i in range(1, N+1):
        # Compute A: subarrays including i
        A = [prefix[r] - prefix[l-1] for l in range(1, i+1) for r in range(i, N+1)]
        # Compute B: subarrays not including i
        B = []
        # Left part: subarrays entirely before 