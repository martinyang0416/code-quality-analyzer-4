def numberOfArithmeticSlices(A):
    if len(A) < 3:
        return 0
    total = 0
    prev_diff = A[1] - A[0]
    current_count = 1  # starts at 1 because we've already computed the first difference
    
    for i in range(2, len(A)):
        current_diff = A[i] - A[i-1]
        if current_diff == prev_diff:
            current_count += 1
        else:
            total += current_count * (current_count - 1) // 2
            prev_diff = current_diff
            current_count = 1
    # Add the l