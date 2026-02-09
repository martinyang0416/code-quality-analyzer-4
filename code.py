import bisect

def putaway(A, B, T, X, Y, W, S):
    if A + B == 0:
        return -1  # According to problem constraints, this won't happen

    sorted_X = sorted(X)
    sorted_Y = sorted(Y)

    Bw = 0  # Toys only assignable to weak
    Cs = 0  # Toys only assignable to small
    A_total = 0  # Toys assignable to either

    for i in range(T):
        w = W[i]
        s = S[i]

        # Check if can be handled by weak robots
        pos_x = bisect.bisect_right(sorted_X, w)
        is_weak = 