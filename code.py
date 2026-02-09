n = int(input())
x1, x2 = map(int, input().split())
functions = []

for _ in range(n):
    a, b, c = map(int, input().split())
    functions.append((a, b, c))

# Check for identical functions
seen = set()
for a, b, c in functions:
    if (a, b, c) in seen:
        print("YES")
        exit()
    seen.add((a, b, c))

u = []
v = []

for a, b, c in functions:
    u_i = a * (x1 ** 2) + b * x1 + c
    v_i = a * (x2 ** 2) + b * x2 + c
    u.append(u_i)
    v.append(v_i)

# Check if any two functions s