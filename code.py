import sys
from collections import defaultdict, deque

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        words = [sys.stdin.readline().strip() for _ in range(n)]
        valid = True
        edges = []
        for i in range(n-1):
            s = words[i]
            t = words[i+1]
            min_len = min(len(s), len(t))
            prefix = True
            for k in range(min_len):
                if s[k] != t[k]:
               