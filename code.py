MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    # Precompute factorials and inverse factorials up to 3999
    max_fact = 3999
    fact = [1] * (max_fact + 1)
    for i in range(1, max_fact + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_fact + 1)
    inv_fact[max_fact] = pow(fact[max_fact], MOD - 2, MOD)
    for i in range(max_fact - 1, -1, -1):
        inv_fact[i] = in