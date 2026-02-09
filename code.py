from collections import defaultdict, Counter

def balancedString(s):
    n = len(s)
    target = n // 4
    total_counts = Counter(s)
    
    if all(total_counts[c] == target for c in 'QWER'):
        return 0
    
    min_len = float('inf')
    window_counts = defaultdict(int)
    left = 0
    
    for right in range(n):
        char = s[right]
        window_counts[char] += 1
        
        while left <= right and all((total_counts[c] - window_counts.get(c, 0)) <= target for c in 'QWER'):
 