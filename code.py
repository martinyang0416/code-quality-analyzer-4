n = int(input())
circles = [tuple(map(int, input().split())) for _ in range(n)]

# Generate all possible k candidates
candidates = set()
for x, y, r in circles:
    candidates.add(x + y)
    candidates.add(x - y)

# Check each candidate k
found = False
for k in candidates:
    valid = True
    for x, y, r in circles:
        if abs(x - k) != y:
            valid = False
            break
    if valid:
        print("t")
        print(f"abs((t-{k}))")
        found = True
        break

# If no v