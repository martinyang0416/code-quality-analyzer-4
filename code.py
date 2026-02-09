import sys

def minimal_changes(s):
    if not s:
        return 0
    total = 0
    current_char = s[0]
    run_length = 1
    for c in s[1:]:
        if c == current_char:
            run_length += 1
        else:
            total += (run_length - 1) // 2
            current_char = c
            run_length = 1
    total += (run_length - 1) // 2
    return total

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        print(minimal_