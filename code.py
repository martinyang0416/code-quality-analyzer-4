import math

x, y, z = map(float, input().split())

expressions = [
    {'index': 1, 'expr': 'x^y^z', 'type': 1, 'A': z * math.log(y), 'B': math.log(x)},
    {'index': 2, 'expr': 'x^z^y', 'type': 1, 'A': y * math.log(z), 'B': math.log(x)},
    {'index': 3, 'expr': '(x^y)^z', 'type': 2, 'log_val': y * z * math.log(x)},
    {'index': 4, 'expr': '(x^z)^y', 'type': 2, 'log_val': z * y * math.log(x)},
    {'index': 5, 'expr': 'y^x^z', 'type': 1, 'A': z * math.log(x), 'B': math.log(y)},
    {'index': 