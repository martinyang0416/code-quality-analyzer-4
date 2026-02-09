n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

if c[0] != t[0] or c[-1] != t[-1]:
    print("No")
else:
    c_diff = [c[i] - c[i-1] for i in range(1, n)]
    t_diff = [t[i] - t[i-1] for i in range(1, n)]
    if sorted(c_diff) == sorted(t_diff):
        print("Yes")
    else:
        print("No")