def numTimesAllBlue(light):
    current_max = 0
    count = 0
    for i in range(len(light)):
        current_max = max(current_max, light[i])
        if current_max == i + 1:
            count += 1
    return count