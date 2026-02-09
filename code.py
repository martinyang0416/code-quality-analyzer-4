from collections import defaultdict

def leastBricks(wall):
    edge_counts = defaultdict(int)
    for row in wall:
        current_sum = 0
        for brick in row[:-1]:
            current_sum += brick
            edge_counts[current_sum] += 1
    max_edges = max(edge_counts.values(), default=0)
    return len(wall) - max_edges