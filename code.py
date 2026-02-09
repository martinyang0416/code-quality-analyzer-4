import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        k, n = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        first = -1
        for i in range(n):
            if arr[i] == k:
                first = i + 1
                break
        last = -1
        for i in range(n-1, -1, -1):
            if arr[i] == k:
                last = i + 1
                break
        if first == -1:
            print(0)
 