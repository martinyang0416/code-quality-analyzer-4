n = int(input())
parts = {}
for _ in range(n):
    part, cost = input().split()
    cost = int(cost)
    parts[part] = cost

m = int(input())
assembly = {}
for _ in range(m):
    # Split the line into machine, k, and components
    parts_line = input().split()
    machine = parts_line[0]
    k = int(parts_line[1])
    components = parts_line[2:2 + k]
    assembly[machine] = components

target = input().strip()

computed = {}

def compute_min(part):
    if part in computed:
        return compute