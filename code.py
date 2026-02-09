def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1

    if m < n - 1:
        print("Impossible")
        return

    islands = []
    for _ in range(n):
        l = int(input[ptr])
        ptr += 1
        r = int(input[ptr])
        ptr += 1
        islands.append((l, r))

    s_list = []
    for i in range(n - 1):
        l_next = islands[i + 1][0]
        r_curr = islands[i][1]
        s = l_ne