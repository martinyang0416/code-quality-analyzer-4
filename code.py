import sys

def main():
    s = sys.stdin.read().strip()
    T = 'bessie'
    n = len(s)
    current_state = 0
    completed = 0
    cnt = [0] * (n + 1)  # cnt[i] is the number of completions after first i characters

    for i in range(n):
        if s[i] == T[current_state]:
            current_state += 1
            if current_state == len(T):
                completed += 1
                current_state = 0  # reset for next possible "bessie"
        cnt[i + 1] = completed

    sum1 = 0
    f