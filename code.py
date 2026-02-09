import bisect

def minSubArrayLen(s, nums):
    n = len(nums)
    if n == 0:
        return 0
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    min_length = float('inf')
    for i in range(len(prefix)):
        target = prefix[i] + s
        j = bisect.bisect_left(prefix, target, i + 1, len(prefix))
        if j != len(prefix):
            min_length = min(min_length, j - i)
    return min_length if min_length != float('inf') else 0