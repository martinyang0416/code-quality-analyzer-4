import math
r1, r2 = map(int, input().split())
r = min(r1, r2)
area = math.pi * r ** 2
print("{0:.10f}".format(area))