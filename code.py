def minOperations(n: int) -> int:
    if n % 2 == 0:
        m = n // 2
        return m * m
    else:
        m = (n - 1) // 2
        return m * (m + 1)