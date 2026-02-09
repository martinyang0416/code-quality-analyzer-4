T = int(input())
for _ in range(T):
    s = input().strip()
    r = s[::-1]
    funny = True
    for i in range(1, len(s)):
        s_diff = abs(ord(s[i]) - ord(s[i-1]))
        r_diff = abs(ord(r[i]) - ord(r[i-1]))
        if s_diff != r_diff:
            funny = False
            break
    print("Funny" if funny else "Not Funny")