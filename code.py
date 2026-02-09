import sys
import math

def main():
    input = sys.stdin.read().split()
    idx = 0
    T, X = map(int, input[idx:idx+2])
    idx += 2
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        abs_N = abs(N)
        S = math.isqrt(abs_N)
        S_sq = S * S
        diff = N - S_sq
        threshold = X * N / 100
        if diff <= threshold:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()