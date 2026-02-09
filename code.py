class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)  # Use +2 to avoid issues with 1-based indexing
    
    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def min_swaps(grid):
    n = len(grid)
    max_pos = 