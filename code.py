def numFriendRequests(ages):
    count = [0] * 121
    for age in ages:
        count[age] += 1
    
    total = 0
    for a in range(1, 121):
        if count[a] == 0:
            continue
        for b in range(1, 121):
            if count[b] == 0:
                continue
            if (b <= 0.5 * a + 7) or (b > a) or (b > 100 and a < 100):
                continue
            if a == b:
                total += count[a] * (count[a] - 1)
            else:
                total += count[a] *