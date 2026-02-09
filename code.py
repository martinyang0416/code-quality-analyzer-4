T = int(input())
for _ in range(T):
    N = int(input())
    activities = input().split()
    valid = True
    for i in range(N):
        if activities[i] == "collect":
            if i == N - 1:
                valid = False
                break
            if activities[i+1] != "sort":
                valid = False
                break
    print("YES" if valid else "NO")