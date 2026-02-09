M = int(input())
B = list(map(int, input().split()))
if len(B) == len(set(B)):
    print("UNIQUE")
else:
    print("DUPLICATE")