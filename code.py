import heapq

n, m = map(int, input().split())
reversed_adj = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    reversed_adj[v].append(u)
    in_degree[u] += 1

heap = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(heap, -i)

labels = [0] * (n+1)
current_label = n

while heap:
    node = -heapq.heappop(heap)
    labels[node] = current_label
    current_label -= 1
    for neighbor in reversed_adj[node]:
     