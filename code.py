import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        break
    arr = []
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        arr.append(num)
    swap_count = 0
    unsorted_len = n
    while unsorted_len > 1:
        for j in range(unsorted_len - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
        unsorted_l