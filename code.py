def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    abs_n = abs(n)
    result = 1.0
    current_product = x
    while abs_n > 0:
        if abs_n % 2 == 1:
            result *= current_product
        current_product *= current_product
        abs_n = abs_n // 2
    return 1 / result if n < 0 else result