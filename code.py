import math

n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
differences = [max_a - x for x in a]

current_gcd = 0
for d in differences:
    current_gcd = math.gcd(current_gcd, d)

z = current_gcd
y = sum(d // z for d in differences)

print(y, z)