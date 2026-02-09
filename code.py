n, k = map(int, input().split())
stacks = []
for _ in range(n):
    b, p = map(int, input().split())
    stacks.append((p, b))

# Sort the stacks based on their positions
stacks.sort()

max_books = 0
current_sum = 0
left = 0

for right in range(len(stacks)):
    current_sum += stacks[right][1]
    
    # Ensure the window is within K distance
    while stacks[right][0] - stacks[left][0] > k:
        current_sum -= stacks[left][1]
        left += 1
    
    # Update the maximum number of books
  