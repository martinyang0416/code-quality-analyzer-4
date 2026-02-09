MOD = 10**9 + 7
inv25 = pow(25, MOD-2, MOD)

T = int(input())
for _ in range(T):
    N = int(input())
    m_odd = (N + 1) // 2
    m_even = N // 2
    
    pow_odd = pow(26, m_odd + 1, MOD)
    sum_odd = (pow_odd - 26) * inv25 % MOD
    
    pow_even = pow(26, m_even + 1, MOD)
    sum_even = (pow_even - 26) * inv25 % MOD
    
    total = (sum_odd + sum_even) % MOD
    print(total)