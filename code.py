a = int(input())
found = 0
n = a
while n > 0:
    d = n % 10
    if d % 3 == 0:
        found = 1
        break
    n = n // 10
print(found)