def putaway(A, B, T, X, Y, W, S):
    # Compute maximums for X and Y arrays
    X_max = max(X) if A > 0 else 0
    Y_max = max(Y) if B > 0 else 0

    C1 = 0  # toys handled only by weak
    C2 = 0  # toys handled only by small
    C3 = 0  # toys handled by either

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = (A > 0) and (w < X_max)
        can_small = (B > 0) and (s < Y_max)
        if can_weak and can_small:
            C3 += 1
        elif can_weak:
            