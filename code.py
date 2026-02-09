import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx]); idx +=1
    a = list(map(int, input[idx:idx+N])); idx +=N
    Q = int(input[idx]); idx +=1
    queries = []
    for _ in range(Q):
        i = int(input[idx])-1  # convert to 0-based
        j = int(input[idx+1])
        queries.append( (i, j) )
        idx +=2

    S = sorted(a)
    prefix_sum = [0]*(N+1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + S[i]
    to