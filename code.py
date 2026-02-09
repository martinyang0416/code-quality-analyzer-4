T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    s = input().strip()
    possible = False
    for i in range(1, n+1):
        for j in range(1, m+1):
            ci, cj = i, j
            valid = True
            for move in s:
                if move == 'L':
                    cj -= 1
                elif move == 'R':
                    cj += 1
                elif move == 'U':
                    ci -= 1
                else:
                    ci += 1
          