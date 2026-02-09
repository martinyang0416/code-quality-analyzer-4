import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    W_only = 0
    S_only = 0
    Both = 0
    
    for i in range(T):
        wi = W[i]
        si = S[i]
        
        is_weak = bisect.bisect_right(X_sorted, wi) < len(X_sorted)
        is_small = bisect.bisect_right(Y_sorted, si) < len(Y_sorted)
        
        if not (is_weak or is_small):
            return -1
        
        if is_weak and is_small:
            Both += 1
        el