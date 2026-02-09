n = int(input())

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0:
        return False
    d = num - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if a >= num:
            continue
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            cont