MOD = 10**9 + 7

def main():
    import sys
    N, K, P = map(int, sys.stdin.readline().split())
    B = list(map(int, sys.stdin.readline().split()))
    
    if N != 2 * K:
        print(0)
        return
    
    if P > N:
        print(0)
        return
    
    from collections import defaultdict
    count_B = defaultdict(int)
    for num in B:
        if num < 1 or num > K:
            print(0)
            return
        count_B[num] += 1
    
    for num in count_B:
        if count_B[num]