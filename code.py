import math

def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        m = N + 1
        d = math.gcd(m, 4)
        print((4 * N) // d)

if __name__ == "__main__":
    main()