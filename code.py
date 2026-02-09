for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    s = input().strip()
    for d in s:
        if d in 'LR':
            new_grid = []
            for row in grid:
                cnt = row.count('1')
                if d == 'L':
                    new_row = '1' * cnt + '0' * (m - cnt)
                else:
                    new_row = '0' * (m - cnt) + '1' * cnt
                new_grid.append(new_row)
            grid = new_g