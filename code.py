def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = sys.stdin.readline().strip()
    U = int(sys.stdin.readline())
    updates = []
    for _ in range(U):
        p, c = sys.stdin.readline().split()
        updates.append((int(p)-1, c))  # convert to 0-based index

    def compute_A(s):
        target = ['b','e','s','s','i','e']
        m = len(target)
        n = len(s)
        last = [-1] + [-1]*(m)  # last[0] is the base, last[1..m] tracks progress
        count = [0]*(n+1) 