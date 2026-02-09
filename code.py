MOD = 10**9 + 7

def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    tests = []
    for _ in range(M):
        s = sys.stdin.readline().strip()
        tests.append(s)
    
    # Compute bitmask for each problem
    bitmask = []
    for j in range(N):
        b = 0
        for i in range(M):
            c = tests[i][j]
            if c == 'H':
                b |= (1 << i)
        bitmask.append(b)
    
    # Count frequency of each bitmask
    from collections impor