def uniquePaths(m, n):
    a = m + n - 2
    k = min(m - 1, n - 1)
    numerator = 1
    for i in range(k):
        numerator *= (a - i)
    denominator = 1
    for i in range(1, k + 1):
        denominator *= i
    return numerator // denominator