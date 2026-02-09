import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        l = int(sys.stdin.readline())
        # Read the edges but ignore them
        for _ in range(l):
            u, v = map(int, sys.stdin.readline().split())
        if l > n - 1:
            print("CYCLE DETECTED.")
        else:
            print("NO CYCLE.")

if __name__ == "__main__":
    main()