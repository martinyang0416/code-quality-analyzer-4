from collections import defaultdict

def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    count = defaultdict(int)
    n = len(s)
    min_len = minSize  # Focus on minSize to optimize
    for i in range(n - min_len + 1):
        substr = s[i:i+min_len]
        unique_chars = len(set(substr))
        if unique_chars <= maxLetters:
            count[substr] += 1
    return max(count.values()) if count else 0