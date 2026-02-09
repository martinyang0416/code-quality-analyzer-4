n = int(input())
arr = list(map(int, input().split()))
S = set(arr)

for y in S:
    if arr[y - 1] != y:
        print(-1)
        exit()

m = len(S)
h_list = sorted(S)
y_to_idx = {y: i+1 for i, y in enumerate(h_list)}
g = [y_to_idx[val] for val in arr]

print(m)
print(' '.join(map(str, g)))
print(' '.join(map(str, h_list)))