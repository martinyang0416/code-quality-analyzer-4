import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx]); idx +=1
    K = int(input[idx]); idx +=1
    T = int(input[idx]); idx +=1

    A = list(map(int, input[idx:idx+K]))
    idx += K

    # Precompute f for each b in 0..N-1
    f = [0] * N
    for b in range(N):
        # Check if b is in A using bisect
        pos = bisect.bisect_left(A, b)
        if pos < K and A[pos] == b:
            # found in A at index pos
            j = pos
