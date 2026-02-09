import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    can_weak = []
    can_small = []
    
    for w in W:
        idx = bisect.bisect_right(X_sorted, w)
        can_weak.append(idx < len(X_sorted))
    
    for s in S:
        idx = bisect.bisect_right(Y_sorted, s)
        can_small.append(idx < len(Y_sorted))
    
    # Check if any toy can't be assigned to any
    for i in range(T):
        if not (can_weak[i] or can_small[i]):
          