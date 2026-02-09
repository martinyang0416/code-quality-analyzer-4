import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n = int(line.strip())
        if n == 0:
            break
        colors = list(map(int, sys.stdin.readline().strip().split()))
        dp = [[0] * n for _ in range(n)]
        
        for l in range(2, n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                max_val = 0
                # Check pair starting at i
                if colors[