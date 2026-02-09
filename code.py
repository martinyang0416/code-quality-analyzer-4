import sys
from bisect import bisect_right

def main():
    sys.setrecursionlimit(1 << 25)
    t = sys.stdin.readline().strip()
    N = len(t)
    U = int(sys.stdin.readline())
    updates = []
    for _ in range(U):
        p, c = sys.stdin.readline().split()
        p = int(p) - 1  # converting to 0-based index
        updates.append((p, c))
    
    # We need to compute the sum A(t) initially, and then after each update.
    # To handle this, we can track the current state of the string and c