n = int(input())
a = list(map(int, input().split()))
min_candidate = None

for x in range(1, 1001):
    temp = a + [x]
    temp_sorted = sorted(temp)
    if min_candidate is None or temp_sorted < min_candidate:
        min_candidate = temp_sorted.copy()

print(' '.join(map(str, min_candidate)))