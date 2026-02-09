def minOperations(nums):
    sum_bits = 0
    max_bit = 0
    for num in nums:
        if num == 0:
            continue
        sum_bits += bin(num).count('1')
        current_bit = num.bit_length()
        if current_bit > max_bit:
            max_bit = current_bit
    return sum_bits + max(0, max_bit - 1)