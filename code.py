v, e, r = map(int, input().split())
edges = []
for _ in range(e):
    s, t, w = map(int, input().split())
    edges.append((s, t, w))

def find_min_arborescence(nodes, edges, root):
    if len(nodes) == 1:
        return 0

    min_incoming = {}
    for node in nodes:
        if node == root:
            continue
        incoming = [(s, t, w) for s, t, w in edges if t == node]
        if not incoming:
            return float('inf')
        min_edge = min(incoming, key=lambda x: x[2])
        mi