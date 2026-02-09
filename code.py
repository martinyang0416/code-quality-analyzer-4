n, m = map(int, input().split())

if m == 0:
    print(0 if n == 1 else -1)
else:
    parent = list(range(n + 1))  # 1-based indexing

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]  # Path compression
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root != v_root:
            parent[v_root] = u_root

    for _ in range(m):
        u, v, w = map(int, input().split())
        