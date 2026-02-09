n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
row_sums = [sum(row) for row in grid]
column_sums = [sum(col) for col in zip(*grid)]
count = 0
for i in range(n):
    for j in range(n):
        if column_sums[j] > row_sums[i]:
            count += 1
print(count)