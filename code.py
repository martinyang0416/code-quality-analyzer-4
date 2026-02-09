MOD = 10**9 + 7
max_fact = 4000

# Precompute factorials and inverse factorials up to max_fact
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
for i in range(max_fact - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# Read input
N, K = map(int, input().split())
total_n = N + K - 1

# Calculate combination
result = fact[total_n] * inv_fact[K] % MOD
r