n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Collect all non-zero elements from the matrix (excluding diagonal)
S = set()
for i in range(n):
    for j in range(n):
        if i != j:
            S.add(matrix[i][j])

# Determine M as the missing number in 1..n
M = None
for num in range(1, n+1):
    if num not in S:
        M = num
        break

K = max(S)  # Second maximum element

# Calculate row_max for each row
row_max = [