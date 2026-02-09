import sys
import math

def get_gcd(arr):
    from math import gcd
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            break
    return current_gcd

def get_divisors(g):
    if g == 0:
        return []
    factors = {}
    i = 2
    while i * i <= g:
        while g % i == 0:
            factors[i] = factors.get(i, 0) + 1
            g = g // i
        i += 1
    if g > 1:
        factors[g] = 1
    divisors = [1]