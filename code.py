def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    
    steps = 0
    while True:
        next_a = a.copy()
        changed = False
        for i in range(1, n-1):
            s = a[i-1] + a[i] + a[i+1]
            new_val = 1 if s >= 2 else 0
            if new_val != a[i]:
                changed = True
                next_a[i] = new_val
        if not changed:
            break
        a = next_a
        steps += 1
 