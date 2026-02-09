def get_char(n, k):
    f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"
    L0 = 75
    
    if n == 0:
        if k <= L0:
            return f0[k-1]
        else:
            return '.'
    
    # Compute L_{n-1} iteratively to avoid recursion
    L_prev = L0
    for i in range(1, n):
        L_prev = 2 * L_prev + 68
    current_L = 2 * L_prev + 68
    
    if k > current_L:
        return '.'
    
    A_len = 33
    first_part_len = A_len + (1 + L_prev + 1 +