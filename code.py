T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    i = j = 0
    merged = []
    while i < N and j < M:
        if A[i] >= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    merged.extend(A[i:])
    merged.extend(B[j:])
    print(' '.join(map(str, merged)))