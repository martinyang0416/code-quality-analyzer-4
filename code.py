def putaway(A, B, T, X, Y, W, S):
    import sys

    max_x = -float('inf')
    if A > 0:
        max_x = max(X)
    max_y = -float('inf')
    if B > 0:
        max_y = max(Y)

    W_only = 0
    S_only = 0
    Both = 0

    for i in range(T):
        w = W[i]
        s = S[i]

        can_weak = (w < max_x)
        can_small = (s < max_y)

        if not can_weak and not can_small:
            return -1
        if can_weak and can_small:
            Both += 1
        elif can_weak:
            