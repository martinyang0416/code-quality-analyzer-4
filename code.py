s = input().strip()
target = 'keyence'

for i in range(len(target) + 1):
    prefix = target[:i]
    suffix = target[i:]
    if s.startswith(prefix) and s.endswith(suffix):
        print("YES")
        exit()

print("NO")