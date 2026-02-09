def main():
    import sys
    N, K, T, U = map(int, sys.stdin.readline().split())
    H = list(map(int, sys.stdin.readline().split()))
    
    cut_list = []
    for h in H:
        if h < T:
            cut_list.append(h)
    
    max_allowed = N - K
    if len(cut_list) <= max_allowed:
        print(len(cut_list))
        return
    
    # Re-evaluation process
    # Start from the end of the cut_list and check in reverse
    i = len(cut_list) - 1
    while i >= 0 and len(cut_list) > max_allo