a = int(input())
weights = [1, 2, 23, 24, 25, 47]
binary_str = format(a, '06b')
total = 0
for i in range(6):
    if binary_str[i] == '1':
        bit_num = 5 - i
        total += weights[bit_num]
print(total)