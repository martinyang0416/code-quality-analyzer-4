import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b, n = map(int, sys.stdin.readline().split())
        if n == 0:
            print(a)
        else:
            rem = n % 3
            if rem == 0:
                print(a)
            elif rem == 1:
                print(b)
            else:
                print(a ^ b)

if __name__ == "__main__":
    main()