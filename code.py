from collections import deque

def main():
    s = input().strip()
    target = list("bessie")  # The target sequence to form
    n = len(s)
    steps = [deque() for _ in range(7)]  # steps[0] to steps[6]
    completed = []

    for R in range(n):
        c = s[R]
        # Process the current character for each possible step backward
        for i in range(5, -1, -1):
            if c == target[i]:
                if steps[i]:
                    start = steps[i].popleft()
                    i