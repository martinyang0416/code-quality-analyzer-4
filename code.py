def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        D = int(input[idx+1])
        idx +=2
        X = list(map(int, input[idx:idx+N]))
        idx += N
        current = D
        for x in reversed(X):
            current = current // x * x
        print(current)

if __name__ == "__main__":
    main()