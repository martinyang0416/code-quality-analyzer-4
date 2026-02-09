import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    unique = set(arr)
    required = len(unique)
    if required == 0:
        print("1 1")
        return

    current_counts = defaultdict(int)
    have = 0
    min_length = float('inf')
    result = (0, 0)
    left = 0

    for right in range(n):
        el = arr[right]
        current_counts[el] += 1
        if current_counts[el] == 1:
         