import collections

def longestSubstring(s, k):
    if len(s) < k:
        return 0
    count = collections.Counter(s)
    invalid_chars = [char for char in count if count[char] < k]
    if not invalid_chars:
        return len(s)
    splits = []
    start = 0
    for i, c in enumerate(s):
        if c in invalid_chars:
            if start < i:
                splits.append(s[start:i])
            start = i + 1
    if start < len(s):
        splits.append(s[start:])
    max_len = 0
    for spli