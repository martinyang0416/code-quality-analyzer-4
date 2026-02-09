n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
chosen = list(map(int, input().split()))

max_in_school = {}
for i in range(n):
    school = s[i]
    power = p[i]
    if school not in max_in_school or power > max_in_school[school]:
        max_in_school[school] = power

count = 0
for c in chosen:
    idx = c - 1
    school = s[idx]
    if p[idx] < max_in_school.get(school, 0):
        count += 1

print(count)