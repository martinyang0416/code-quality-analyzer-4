# Read the number of test cases
t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    # Check if there's any common character
    if set(a) & set(b):
        print("Yes")
    else:
        print("No")