import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        c = min(k, m-1)
        s = (m-1) - c
        max_x = 0
        for a in range(c + 1):
            current_min = float('inf')
            for a_prime in range(s + 1):
                left = a + a_prime
                right = left + (n - m)
                current_max = max(arr[left], arr[right