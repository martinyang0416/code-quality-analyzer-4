L = int(input())
k = L // 2
h = 2
required_cuts = k - 1
positions = [h * i for i in range(1, required_cuts + 1)]
di = [int(input()) for _ in range(L - 1)]
total = 0

for pos in positions:
    if pos <= len(di):  # Ensure position is within the available di indices
        total += di[pos - 1]

print(total)