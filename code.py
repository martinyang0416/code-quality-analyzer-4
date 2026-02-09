import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    res = []
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        if (n - 1) % (k + 1) == 0:
            res.append("Nandu")
        else:
            res.append("Rani")
    print('\n'.join(res))

if __name__ == "__main__":
    main()