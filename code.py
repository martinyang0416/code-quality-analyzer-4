a = int(input())
bits = [0] * 6
for i in range(6):
    bits[i] = (a >> i) & 1

new_bits = [
    bits[3],  # output0
    bits[1],  # output1
    bits[4],  # output2
    bits[2],  # output3
    bits[0],  # output4
    bits[5],  # output5
]

result = 0
for i in range(6):
    result += new_bits[i] << i

print(result)