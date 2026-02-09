def rotate_right(s, N):
    return (s >> 1) | ((s & 1) << (N - 1))

def main():
    import sys
    from collections import deque

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    for _ in range(T):
        L_str = input[idx]
        S_str = input[idx + 1]
        idx += 2

        L0 = int(L_str, 2)
        S0 = int(S_str, 2)

        visited = set()
        q = deque()
        initial_state = (S0, 0)
        q.append