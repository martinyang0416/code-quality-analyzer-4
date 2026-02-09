def findLongestWord(s, d):
    def is_subsequence(word):
        i = j = 0
        n, m = len(s), len(word)
        while i < n and j < m:
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == m
    
    d_sorted = sorted(d, key=lambda x: (-len(x), x))
    for word in d_sorted:
        if is_subsequence(word):
            return word
    return ""