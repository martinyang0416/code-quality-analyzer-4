t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [input().strip() for _ in range(n)]
    star_row, star_col = 0, 0
    for i in range(n):
        if '*' in matrix[i]:
            star_row = i
            star_col = matrix[i].index('*')
            break
    m = n // 2
    print(abs(star_row - m) + abs(star_col - m))