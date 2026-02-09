def decodeAtIndex(S, K):
    stack = []
    current_length = 0
    for c in S:
        if c.isalpha():
            current_length += 1
            stack.append(c)
            if current_length == K:
                return c
        else:
            d = int(c)
            if current_length * d < K:
                current_length *= d
                stack.append(c)
            else:
                current_length *= d
                stack.append(c)
                break
    
    while stack:
  