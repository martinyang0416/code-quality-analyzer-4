def putaway(A, B, T, X, Y, W, S):
    import sys
    if T == 0:
        return 0  # Not possible per problem constraints, but handled.

    max_x = -sys.maxsize
    if A > 0:
        max_x = max(X)
    max_y = -sys.maxsize
    if B > 0:
        max_y = max(Y)

    O_w = 0
    O_s = 0
    M = 0

    for i in range(T):
        can_weak = (A > 0) and (W[i] < max_x)
        can_small = (B > 0) and (S[i] < max_y)
        if not can_weak and not can_small:
            return -1
        if can_weak and