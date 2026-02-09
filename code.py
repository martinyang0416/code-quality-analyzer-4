import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    M = int(data[idx])
    idx += 1
    D = int(data[idx])
    idx += 1
    
    sites = []
    for _ in range(M):
        r = int(data[idx])
        p = int(data[idx + 1])
        sites.append((r, p))
        idx += 2
    
    # Sort the sites based on position
    sites.sort(key=lambda x: x[1])
    
    p_list = [p for (r, p) in sites]
    r_list = [r for (r, p) in sites]
    
    # Comp