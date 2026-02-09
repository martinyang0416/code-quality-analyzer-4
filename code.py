n = int(input())
s = input().strip()

result = []
used = set()
current_start = 0

while True:
    max_char = None
    max_pos = -1
    # Iterate through the current segment to find the highest available character
    for i in range(current_start, n):
        c = s[i]
        if c not in used:
            if max_char is None or c > max_char:
                max_char = c
                max_pos = i
    if max_char is None:
        break  # No more characters can be added
    result.append(max_char