import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    s = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    u = int(data[idx])
    idx += 1
    v = int(data[idx])
    idx += 1

    edges = [[] for _ in range(n + 1)]
    original_edges = []
    for _ in range(m):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
  