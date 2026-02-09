import sys

def main():
    n = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))
    s = list(map(int, sys.stdin.readline().split()))
    
    max_sum = 0
    
    for i in range(n):
        a = c[i]
        sa = s[i]
        for j in range(i + 1, n):
            b = c[j]
            sb = s[j]
            # Check if neither a is subset of b nor b is subset of a
            intersect = a & b
            if (intersect == a) or (intersect == b):
                continu