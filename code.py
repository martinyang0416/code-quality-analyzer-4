def scoreOfParentheses(S):
    stack = []
    for char in S:
        if char == '(':
            stack.append(0)
        else:
            popped = stack.pop()
            current = 1 if popped == 0 else 2 * popped
            if stack:
                stack[-1] += current
            else:
                stack.append(current)
    return sum(stack)