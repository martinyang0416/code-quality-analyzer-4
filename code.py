n = int(input())
events = []
for _ in range(n):
    s, d = map(int, input().split())
    end = s + d - 1
    events.append((end, s))

events.sort()

count = 0
last_end = 0

for end, start in events:
    if start > last_end:
        count += 1
        last_end = end

print(count)