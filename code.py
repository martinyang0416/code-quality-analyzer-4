def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = input[idx]
    idx += 1
    U = int(input[idx])
    idx += 1
    updates = []
    for _ in range(U):
        p = int(input[idx])-1  # converting to 0-based
        c = input[idx+1]
        updates.append((p, c))
        idx +=2

    def compute_count(s):
        T = ['b', 'e', 's', 's', 'i', 'e']
        n = len(s)
        count = [0]*(n)
        current_ptr = 0
        current_count = 0
        for i in range(n)