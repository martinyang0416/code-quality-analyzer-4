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
    specials = input[idx]
    idx += 1

    # Parse L and R indices
    L_indices = []
    R_indices = []
    for i in range(2 * N):
        if S[i] == 'L':
            L_indices.append(i)
        else:
            R_indices.append(i)

    # Compute ℓ and r arrays
    ell = [(L_indices[i] + 1) for i i