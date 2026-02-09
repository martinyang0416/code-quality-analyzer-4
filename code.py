def putaway(A, B, T, X, Y, W, S):
    class Edge:
        __slots__ = ['to', 'rev', 'capacity']
        def __init__(self, to, rev, capacity):
            self.to = to
            self.rev = rev
            self.capacity = capacity

    class Dinic:
        def __init__(self, n):
            self.size = n
            self.graph = [[] for _ in range(n)]
        
        def add_edge(self, fr, to, cap):
            forward = Edge(to, len(self.graph[to]), cap)
            backward = Edge(fr, len(se