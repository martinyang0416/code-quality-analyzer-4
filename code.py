L = int(input())
N = int(input())
for _ in range(N):
    W, H = map(int, input().split())
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    else:
        print("ACCEPTED" if W == H else "CROP IT")