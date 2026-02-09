import collections

def leastInterval(tasks, n):
    freq = collections.Counter(tasks)
    max_freq = max(freq.values(), default=0)
    max_count = sum(1 for v in freq.values() if v == max_freq)
    part1 = (max_freq - 1) * (n + 1) + max_count
    part2 = len(tasks)
    return max(part1, part2)