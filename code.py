def longestWPI(hours):
    scores = [1 if h > 8 else -1 for h in hours]
    n = len(scores)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + scores[i]
    
    stack = [0]
    for i in range(1, n):
        if prefix[i] < prefix[stack[-1]]:
            stack.append(i)
    
    max_len = 0
    for j in range(1, len(prefix)):
        low, high = 0, len(stack) - 1
        best_i = -1
        while low <= high:
            mid = (low + high) // 2
            if pref