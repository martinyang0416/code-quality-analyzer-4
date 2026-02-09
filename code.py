def count_digit_one(n):
    count = 0
    i = 0
    while 10**i <= n:
        divisor = 10 ** (i + 1)
        higher = n // divisor
        current = (n // (10**i)) % 10
        lower = n % (10**i)
        if current < 1:
            count += higher * (10**i)
        elif current == 1:
            count += higher * (10**i) + lower + 1
        else:
            count += (higher + 1) * (10**i)
        i += 1
    return count