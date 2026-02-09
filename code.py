def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        W = list(map(int, input[idx:idx+N]))
        idx += N
        max_v = 0
        for i in range(N):
            current = W[i] + i
            if current > max_v:
                max_v = current
        print(max_v)

if __name__ == "__main__":
    main()