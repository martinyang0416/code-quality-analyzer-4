def find_min_y0(y2):
    def get_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors

    min_y0 = float('inf')

    p2_list = get_prime_factors(y2)

    for p2 in p2_list:
        lower = y2
        upper = y2 + p2
        for y1 in range(lower, upper):
            if p2 >= y1:
                co