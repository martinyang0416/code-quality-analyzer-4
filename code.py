def getMaxLen(nums):
    segments = []
    current = []
    for num in nums:
        if num == 0:
            if current:
                segments.append(current)
                current = []
        else:
            current.append(num)
    if current:
        segments.append(current)
    
    max_length = 0
    for seg in segments:
        negatives = [i for i, x in enumerate(seg) if x < 0]
        count = len(negatives)
        if count % 2 == 0:
            candidate = len(seg)
        else: