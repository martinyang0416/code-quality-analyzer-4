mod = 10**9 + 9

n, w, b = map(int, input().split())

max_fact = 8000  # Sufficiently large to cover all possible combinations

# Precompute factorial and inverse factorial modulo 10^9+9
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % mod

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], mod-2, mod)
for i in range(max_fact - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % mod

def comb(n, k):
    if k < 0 or k > n:
        