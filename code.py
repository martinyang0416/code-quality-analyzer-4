import bisect

def minimal_operations():
    n, m = map(int, input().split())
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))
    
    seq1.sort()
    seq2.sort()
    
    prefix1 = [0] * (n + 1)
    for i in range(n):
        prefix1[i + 1] = prefix1[i] + seq1[i]
    
    prefix2 = [0] * (m + 1)
    for i in range(m):
        prefix2[i + 1] = prefix2[i] + seq2[i]
    
    def compute_cost(X):
        # Calculate cost for seq1: sum(max(0, a - X) for a in seq