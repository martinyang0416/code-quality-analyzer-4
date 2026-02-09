def reverseParentheses(s: str) -> str:
    stack = []
    current_str = ''
    for char in s:
        if char == '(':
            stack.append(current_str)
            current_str = ''
        elif char == ')':
            current_str = stack.pop() + current_str[::-1]
        else:
            current_str += char
    return current_str