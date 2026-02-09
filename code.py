T = int(input())
for _ in range(T):
    N, K, V = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    required_total = V * (N + K)
    delta = required_total - sum_A
    if delta <= 0 or delta % K != 0:
        print(-1)
    else:
        x = delta // K
        print(x)