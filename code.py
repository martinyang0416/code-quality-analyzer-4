mod_val = 1 << 58

def multiply(a, b):
    res = [0] * 10
    for i in range(10):
        if a[i] == 0:
            continue
        for j in range(10):
            if b[j] == 0:
                continue
            k = (i + j) % 10
            res[k] = (res[k] + a[i] * b[j]) % mod_val
    return res

def power(poly, exponent):
    result = [0] * 10
    result[0] = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = multiply(result, poly)
        poly = multiply(poly, po