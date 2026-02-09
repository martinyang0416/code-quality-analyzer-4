T = int(input())
for _ in range(T):
    K = int(input())
    for i in range(K):
        row = [' '] * K
        for j in range(K):
            if j == 0 or j == K-1 or j == i or j == (K-1 - i):
                row[j] = '1'
        print(''.join(row))