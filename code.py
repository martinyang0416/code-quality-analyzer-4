l, r = map(int, input().split())

if l == r:
    n = l
    if n % 2 == 0:
        print(2)
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                print(i)
                exit()
            i += 2
        print(n)
else:
    print(2)