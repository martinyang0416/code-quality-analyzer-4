def minOperations(target):
    res = 0
    prev = 0
    for num in target:
        diff = num - prev
        if diff > 0:
            res += diff
        prev = num
    return res