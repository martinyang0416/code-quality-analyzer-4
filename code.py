import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
max_val = max(a)
max_count = a.count(max_val)
second_max = -float('inf')

for num in a:
    if num < max_val and num > second_max:
        second_max = num

for num in a:
    if num < max_val:
        print(max_val)
    else:
        if max_count > 1:
            print(max_val)
        else:
            print(second_max if second_max != -float('inf') else max_val)