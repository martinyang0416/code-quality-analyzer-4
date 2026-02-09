import math

a, b, t = map(int, input().split())
gcd = math.gcd(a, b)
lcm = a * b // gcd
result = t // lcm
print(result)