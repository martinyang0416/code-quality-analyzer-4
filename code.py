import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx +=2
        A = list(map(int, input[idx:idx+N]))
        idx += N
        
        found = False
        if K in A:
            print("YES")
            continue
        
        for i in range(N):
            m = A[i]
            if m > K:
                continue
            new_list = A[:i] + A[i+1:]
