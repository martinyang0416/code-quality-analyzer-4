import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    M = int(input[idx])
    idx += 1
    D = int(input[idx])
    idx += 1
    
    spots = []
    for _ in range(M):
        b = int(input[idx])
        idx += 1
        p = int(input[idx])
        idx += 1
        spots.append((p, b))
    
    # Sort spots by position
    spots.sort()
    positions = [spot[0] for spot in spots]
    b_list = [spot[1] for spot in spots]
    
    # Compute prefix sums
    pr