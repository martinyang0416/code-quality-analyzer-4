s = input().strip()
result = []
for c in s:
    digit = int(c)
    if digit % 2 == 0:
        result.append(f'({c})')
    else:
        result.append(c)
print(''.join(result))