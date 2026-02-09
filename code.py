def maxWidthRamp(A):
    sorted_inds = sorted(range(len(A)), key=lambda i: (A[i], i))
    max_width = 0
    current_min = float('inf')
    for j in sorted_inds:
        if j < current_min:
            current_min = j
        else:
            max_width = max(max_width, j - current_min)
    return max_width