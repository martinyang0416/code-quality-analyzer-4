def countVowelPermutation(n: int) -> int:
    mod = 10**9 + 7
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(n - 1):
        a_new = (e + i + u) % mod
        e_new = (a + i) % mod
        i_new = (e + o) % mod
        o_new = i % mod
        u_new = (i + o) % mod
        a, e, i, o, u = a_new, e_new, i_new, o_new, u_new
    return (a + e + i + o + u) % mod