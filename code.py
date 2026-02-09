n = int(input())
concerts = []
for _ in range(n):
    a, b = map(int, input().split())
    concerts.append((a, b))

# Sort by scheduled date (a_i)
concerts.sort()

prev = 0
last_day = 0
for a, b in concerts:
    current = max(prev, b)
    # Ensure current does not exceed a_i
    if current > a:
        current = a
    if current < prev:
        current = prev  # Ensure non-decreasing
    last_day = current
    prev = current

print(last_day)