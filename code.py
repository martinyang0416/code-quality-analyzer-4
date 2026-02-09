def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # Remove remaining k digits from the end
    if k > 0:
        stack = stack[:-k]
    # Convert to string and remove leading zeros
    result = ''.join(stack).lstrip('0')
    return result if result else '0'