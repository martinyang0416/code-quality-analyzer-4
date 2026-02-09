def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    h = list(map(int, input[1:n+1]))
    
    next_tree = [ -1 ] * n
    
    # Compute next shorter tree for each position using a stack
    stack = []
    for i in range(n-1, -1, -1):
        while stack and h[stack[-1]] >= h[i]:
            stack.pop()
        if stack:
            next_tree[i] = stack[-1]
        else:
            next_tree[i] = -1
        stack.append(i)
    
    # Now determine which tree