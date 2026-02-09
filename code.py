# Read the number of test cases
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ones = [i + 1 for i, val in enumerate(A) if val == 1]
    safe = True
    for i in range(1, len(ones)):
        if ones[i] - ones[i-1] < 6:
            safe = False
            break
    print("YES" if safe else "NO")