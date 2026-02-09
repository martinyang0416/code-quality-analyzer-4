import math

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        x = list(map(int, input().split()))
        P, Q = map(int, input().split())
        x.sort()
        total = 0.0
        for i in range(n // 2):
            a = x[i]
            b = x[n - 1 - i]
            dx1 = a - P
            dx2 = b - P
            dot_product = dx1 * dx2 + Q * Q
            mag1 = math.hypot(dx1, Q)
            mag2 = math.hypot(dx2, Q)
            if mag1 == 0 or mag2 =