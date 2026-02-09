class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree_w = [0] * (self.n + 1)
        self.tree_v = [0] * (self.n + 1)
    
    def update(self, idx, delta_w, delta_v):
        idx += 1
        while idx <= self.n:
            self.tree_w[idx] += delta_w
            self.tree_v[idx] += delta_v
            idx += idx & -idx
    
    def query(self, idx):
        idx += 1
        sum_w = 0
        sum_v = 0
        while idx > 0:
            sum_w += self.tree_w[i