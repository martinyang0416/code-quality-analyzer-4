def putaway(A, B, T, X, Y, W, S):
    if T == 0:
        return 0

    max_x = -1
    if A > 0:
        max_x = max(X)
    max_y = -1
    if B > 0:
        max_y = max(Y)

    count_w_only = 0
    count_s_only = 0
    count_both = 0

    for i in range(T):
        can_weak = False
        if A > 0:
            can_weak = W[i] < max_x
        can_small = False
        if B > 0:
            can_small = S[i] < max_y

        if not can_weak and not can_small:
            return -1

        if can_w