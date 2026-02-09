def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    for i in range(1, T+1):
        n = input[i].strip()
        count = sum(1 for c in n if c not in {'4', '7'})
        print(min(count, 1 + count))

if __name__ == "__main__":
    main()