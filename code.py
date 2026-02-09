import sys

def calculate_difference(s):
    if not s:
        return 0
    groups = []
    current_char = s[0]
    count = 1
    for c in s[1:]:
        if c == current_char:
            count += 1
        else:
            groups.append((current_char, count))
            current_char = c
            count = 1
    groups.append((current_char, count))
    
    compressed_size = 0
    for char, cnt in groups:
        compressed_size += 8
        if cnt >= 2:
            compressed_size += 32 * le