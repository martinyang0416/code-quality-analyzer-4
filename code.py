from collections import Counter

def is_dynamic(s):
    freq = list(Counter(s).values())
    freq.sort()
    n = len(freq)
    if n < 3:
        return True
    if n == 3:
        return freq[0] + freq[1] == freq[2]
    else:
        # Check two possible permutations: original and first two swapped
        def check_sequence(lst):
            for i in range(2, len(lst)):
                if lst[i] != lst[i-1] + lst[i-2]:
                    return False
            return True
        
        # 