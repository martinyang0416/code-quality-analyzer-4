from collections import Counter

def canDivideIntoSubsequences(nums, k):
    n = len(nums)
    if n % k != 0:
        return False
    count = Counter(nums)
    unique_nums = sorted(count.keys())
    for num in unique_nums:
        if count[num] == 0:
            continue
        cnt = count[num]
        for i in range(k):
            current = num + i
            if count[current] < cnt:
                return False
            count[current] -= cnt
    return True