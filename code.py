n = int(input())
if n % 2 != 0:
    print("NO")
else:
    print("YES")
    for i in range(1, n, 2):
        a = i
        b = i + 1
        print(a, b)
        print(b, a)