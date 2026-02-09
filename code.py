import sys

def find_max_subarray(arr):
    max_sum = -1
    max_length = 0
    max_start = 0
    max_end = 0
    current_sum = 0
    current_length = 0
    current_start = -1

    n = len(arr)
    for i in range(n):
        num = arr[i]
        if num >= 0:
            if current_start == -1:
                current_start = i
                current_sum = num
                current_length = 1
            else:
                current_sum += num
                current_length += 1
            
