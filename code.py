a = input().strip()
count = 0
for c in a:
    digit = int(c)
    if digit % 2 == 0:
        count += 1
print(0 if count >= 2 else 1)