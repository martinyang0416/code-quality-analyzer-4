import math

a, b, c = map(int, input().split())

if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        x = -c / b
        print(1)
        print("{0:.10f}".format(x))
else:
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print(0)
    elif discriminant == 0:
        x = (-b) / (2 * a)
        print(1)
        print("{0:.10f}".format(x))
    else:
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b - sqrt