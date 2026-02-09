def maxSideLength(mat, threshold):
    m = len(mat)
    n = len(mat[0])
    # Create prefix sum matrix
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    max_k = 0
    low, high = 1, min(m, n)
    while low <= high:
        mid = (low + high) // 2
        found = False
        # Check all possible squares of size mid x mid
        