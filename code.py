a = input().strip()
if any(c in {'2', '3', '5', '7'} for c in a):
    print(1)
else:
    print(0)