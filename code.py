def putaway(A, B, T, X, Y, W, S):
    # Compute maximum X and Y
    max_X = -float('inf')
    if A > 0:
        max_X = max(X)
    max_Y = -float('inf')
    if B > 0:
        max_Y = max(Y)
    
    W_only = 0
    S_only = 0
    J = 0

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = (w < max_X) if A > 0 else False
        can_small = (s < max_Y) if B > 0 else False

        if not can_weak and not can_small:
            return -1
        elif can_weak and not can_smal