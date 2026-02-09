from collections import Counter

def frequency_sort(s):
    counts = Counter(s)
    sorted_chars = sorted(counts.keys(), key=lambda c: (-counts[c], c))
    return ''.join([char * counts[char] for char in sorted_chars])