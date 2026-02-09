def putaway(A, B, T, X, Y, W, S):
    if A == 0:
        max_X = -1
    else:
        max_X = max(X)
    if B == 0:
        max_Y = -1
    else:
        max_Y = max(Y)
    
    W_only = 0
    S_only = 0
    Both = 0
    
    for i in range(T):
        w = W[i]
        s = S[i]
        eligible_weak = (max_X > w)
        eligible_small = (max_Y > s)
        
        if not eligible_weak and not eligible_small:
            return -1
        
        if eligible_weak and not eligible_small:
       