MOD = 10**6 + 3
max_fact = MOD - 1
fact = [1] * (max_fact + 1)

for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

import sys

input = sys.stdin.read
data = input().split()
T = int(data[0])
index = 1

results = []
for _ in range(T):
    N = int(data[index])
    X = int(data[index+1])
    index += 2
    if N >= MOD:
        results.append(0)
    else:
        res = (X % MOD) * fact[N] % MOD
        results.append(res)

sys.stdout.write('\n'.join(map(str, results)) + '\n')