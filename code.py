import bisect

class BIT:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def find_min_available(a, b, bit):
    low = a
    high = b
    res = -1
    while low <= high: