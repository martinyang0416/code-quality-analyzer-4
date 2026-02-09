import math

def putaway(A, B, T, X, Y, W, S):
    # Compute max X and Y
    if A > 0:
        maxX = max(X)
    else:
        maxX = -1
    if B > 0:
        maxY = max(Y)
    else:
        maxY = -1

    O_w = 0  # toys that can only go to weak
    O_s = 0  # toys that can only go to small
    B_other = 0  # toys that can go to either

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = (A > 0 and w < maxX)
        can_small = (B > 0 and s < maxY)
        if not can_wea