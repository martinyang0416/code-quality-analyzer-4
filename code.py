s = input().strip()
even_sum = 0
odd_sum = 0
for c in s:
    digit = int(c)
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
if even_sum % 2 == 0 and odd_sum % 2 == 1:
    print("Yes")
else:
    print("No")