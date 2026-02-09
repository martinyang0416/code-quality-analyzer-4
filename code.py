from collections import Counter

def minSetSize(arr):
    n = len(arr)
    target = n // 2
    freq = Counter(arr)
    sorted_freq = sorted(freq.values(), reverse=True)
    
    count = 0
    total = 0
    for f in sorted_freq:
        total += f
        count += 1
        if total >= target:
            break
    return count