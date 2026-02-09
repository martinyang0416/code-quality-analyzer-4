s = input().strip()
n = len(s)

# Precompute prefix sums for 'b', 'e', 's', 'i'
prefix_b = [0] * (n + 1)
prefix_e = [0] * (n + 1)
prefix_s = [0] * (n + 1)
prefix_i = [0] * (n + 1)

for i in range(n):
    prefix_b[i+1] = prefix_b[i] + (1 if s[i] == 'b' else 0)
    prefix_e[i+1] = prefix_e[i] + (1 if s[i] == 'e' else 0)
    prefix_s[i+1] = prefix_s[i] + (1 if s[i] == 's' else 0)
    prefix_i[i+1] = prefix_i[i] + (1 if s[i] == 'i' else 0)

total = 0

for i in range(n + 1):
    for j in range(i + 1,