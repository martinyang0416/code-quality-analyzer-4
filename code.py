s = input().strip()
digits = s[1:]  # Extract the six digits after 'A'
sum_digits = sum(int(c) for c in digits)
third_digit = digits[2]  # Third digit (0-based index 2)

if third_digit == '1':
    print(sum_digits + 10)
else:
    print(sum_digits + 1)