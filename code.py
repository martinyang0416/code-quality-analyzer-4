import sys

def count_zeros(n):
    count = 0
    divisor = 5
    while divisor <= n:
        count += n // divisor
        divisor *= 5
    return count

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_zeros(n))