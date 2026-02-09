def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        M = int(input[idx])
        idx += 1
        parts = list(map(int, input[idx:idx + int(input[idx]) + 1]))
        N = parts[0]
        stones = parts[1:N+1]
        stones.sort()
        left = 0
        right = N - 1
        count = 0
        while left <= right:
            if stones[left] + stones[right] <= M:
                left += 1
               