def main():
    import sys
    input = sys.stdin.read().splitlines()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        B = int(input[idx])
        idx += 1
        ops = []
        for _ in range(B):
            s = input[idx].strip().split()
            idx += 1
            if s[0] == 'N':
                ops.append(('N', None))
            else:
                ops.append((s[0], int(s[1])))
        current = {1}
        for op in ops:
            new_set = set()
 