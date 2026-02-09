n, m, k = map(int, input().split())
topics = []
for _ in range(m):
    ai, bi, di = map(int, input().split())
    topics.append((ai, bi))

# Initialize DP for the first step
current_dp = {}
for i in range(m):
    ai, bi = topics[i]
    for x in range(ai, bi + 1):
        key = (i, x)
        total = x
        path = [(i, x)]
        if key not in current_dp or total > current_dp[key][0]:
            current_dp[key] = (total, path)

for step in range(2, n + 1):
    new_dp = {}
    for state in cu