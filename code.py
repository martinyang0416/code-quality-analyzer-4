n, k = map(int, input().split())

type10 = []
type01 = []
type11 = []

for _ in range(n):
    t, a, b = map(int, input().split())
    if a == 1 and b == 1:
        type11.append(t)
    elif a == 1 and b == 0:
        type10.append(t)
    elif a == 0 and b == 1:
        type01.append(t)

# Sort each type and compute prefix sums
type10.sort()
type01.sort()
type11.sort()

prefix10 = [0]
for t in type10:
    prefix10.append(prefix10[-1] + t)

prefix01 = [0]
for t in type01:
    prefix01.append(prefi