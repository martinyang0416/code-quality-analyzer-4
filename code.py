import sys

def find_special_number(M):
    L = (M + 7) // 8
    U = M // 5
    if L > U:
        return "-1"
    else:
        for N in range(L, U + 1):
            temp = M - 5 * N
            if temp % 3 != 0:
                continue
            k = temp // 3
            if k < 0 or k > N:
                continue
            # Form the number
            s = '5' * (N - k) + '8' * k
            return s
        return "-1"

M = int(sys.stdin.readline())
print(find_special_number(M))