M, N = map(int, input().split())
diff = [0] * (M + 2)  # 1-based indexing, size M+2

for _ in range(N):
    A, B, C = map(int, input().split())
    diff[A] += C
    if B + 1 <= M:
        diff[B + 1] -= C

max_height = 0
current = 0

for i in range(1, M + 1):
    current += diff[i]
    if current > max_height:
        max_height = current

print(max_height)