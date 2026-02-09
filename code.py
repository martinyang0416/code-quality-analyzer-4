import bisect

def compute_min_time(robots, toys, max_time):
    robots.sort()
    toys.sort()
    counts = [0] * len(robots)
    for toy in toys:
        idx = bisect.bisect_right(robots, toy)
        if idx >= len(robots):
            return -1  # cannot assign
        # Find first robot from idx with counts < max_time
        found = False
        for i in range(idx, len(robots)):
            if counts[i] < max_time:
                counts[i] += 1
                found = True
                