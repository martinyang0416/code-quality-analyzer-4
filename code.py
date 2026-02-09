# Read the number of test cases
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    else:
        # Calculate using the formula 6N² - 12N + 8
        result = 6 * N * N - 12 * N + 8
        print(result)