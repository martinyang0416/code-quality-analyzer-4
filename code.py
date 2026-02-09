a, b, n = map(int, input().split())

def fib(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, m + 1):
        c = a + b
        a = b
        b = c
    return b

f_n_minus_1 = fib(n - 1)
f_n = fib(n)

result = a * f_n_minus_1 + b * f_n
print(result)