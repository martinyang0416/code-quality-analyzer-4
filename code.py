from collections import deque

m, k = map(int, input().split())
t = input().strip()

visited = [False] * (m + 1)
queue = deque()
queue.append((1, 0))
visited[1] = True

while queue:
    pos, steps = queue.popleft()
    if pos == m:
        print(steps)
        exit()
    for step in range(1, k + 1):
        next_pos = pos + step
        if next_pos > m:
            continue
        if next_pos == m:
            print(steps + 1)
            exit()
        if t[next_pos - 1] == '1' and not visited