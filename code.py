import sys

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0]
    for num in a:
        prefix.append(prefix[-1] + num)
    
    all_sums = []
    for l in range(N):
        for r in range(l, N):
            s = prefix[r+1] - prefix[l]
            all_sums.append((s, l, r))
    
    for i in range(N):
        A = [s for s, l, r in all_sums if l <= i <= r]
        B1_sums = [s for s, l, r in all_sums if r < i]
        B2_sums = [s 