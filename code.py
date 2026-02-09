import sys

def main():
    A, B, T = map(int, sys.stdin.readline().split())
    X = list(map(int, sys.stdin.readline().split())) if A > 0 else []
    Y = list(map(int, sys.stdin.readline().split())) if B > 0 else []
    W = []
    S = []
    for _ in range(T):
        w, s = map(int, sys.stdin.readline().split())
        W.append(w)
        S.append(s)
    
    max_X = max(X) if A else 0
    max_Y = max(Y) if B else 0
    
    W_only = 0
    S_only = 0
    Both = 0
    
    for w, s in zip(W, S