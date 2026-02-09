n, k = map(int, input().split())
s = input().strip()

if n == 0:
    print(0)
    exit()

# Create runs list
runs = []
current = s[0]
count = 1
for c in s[1:]:
    if c == current:
        count += 1
    else:
        runs.append((current, count))
        current = c
        count = 1
runs.append((current, count))

max_len = 0
current_sum = 0
b_count = 0
left = 0

for right in range(len(runs)):
    char, length = runs[right]
    if char == 'b':
        b_count += 1
    current_sum += length
    