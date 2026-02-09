#### Answer to <https://codeforces.com/problemset/problem/251/A>
# import math

# count, bounds = [int(x) for x in input().split(" ")]
# total = 0

# left_index = 0
# right_index = 2
# current = 0

# lst = [int(x) for x in input().split(" ")]
# if lst[0] < 0:
#     delta = 1 - lst[0]
#     lst = [x + delta for x in lst]

# while right_index < len(lst):
#     if lst[right_index] - lst[left_index] <= bounds:
#         right_index += 1
#         continue
#     elements = right_index - left_index - 