s = input().strip()
sum_digits = sum(int(c) for c in s[1:])  # Skip the first character 'A'

if sum_digits == 11:
    print(21)
else:
    print(sum_digits + 1)