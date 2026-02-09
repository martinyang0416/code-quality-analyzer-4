import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    # Compute prefix sums
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i-1] + a[i-1]
    
    subarrays = []
    for l in range(1, N + 1):
        for r in range(l, N + 1):
            s = prefix[r] - prefix[l-1]
            subarrays.append((s, l, r))
    
    for i in range(1, N + 1):
        s_in = []
        s_out = []
        for s, l, r 