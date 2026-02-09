import bisect

def putaway(A, B, T, X, Y, W, S):
    # Sort the weight and size limits of the robots
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    W_only = 0  # Toys that can only be handled by weak robots
    S_only = 0  # Toys that can only be handled by small robots
    Both = 0    # Toys that can be handled by either
    
    for i in range(T):
        w = W[i]
        s = S[i]
        weak_ok = False
        small_ok = False
        
        # Check if any weak robot can handle