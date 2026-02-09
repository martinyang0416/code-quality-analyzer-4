import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = sys.stdin.readline().strip()
        total = sum(int(c) for c in n)
        check = (10 - (total % 10)) % 10
        print(n + str(check))

if __name__ == "__main__":
    main()