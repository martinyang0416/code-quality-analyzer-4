def longestPalindrome(s):
    if not s:
        return ""
    start = 0
    end = 0
    n = len(s)
    for i in range(n):
        # Check for odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        current_len = r - l - 1
        if current_len > end - start:
            start = l + 1
            end = r - 1
        
        # Check for even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n 