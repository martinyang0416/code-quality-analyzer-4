import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    Q = int(input[idx])
    idx += 1

    S = input[idx]
    idx += 1
    spec_str = input[idx]
    idx += 1

    all_L = []
    all_R = []
    for i, c in enumerate(S):
        if c == 'L':
            all_L.append(i)
        else:
            all_R.append(i)

    # Precompute reach array
    reach = [0] * N
    for i in range(N):
        r_i = all_R[i]
        j = bis