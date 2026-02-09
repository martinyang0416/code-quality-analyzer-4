import sys

def main():
    A, B, T = map(int, sys.stdin.readline().split())
    X = []
    Y = []
    if A > 0:
        X = list(map(int, sys.stdin.readline().split()))
    else:
        sys.stdin.readline()  # consume empty line
    if B > 0:
        Y = list(map(int, sys.stdin.readline().split()))
    else:
        sys.stdin.readline()  # consume empty line
    
    W = []
    S = []
    for _ in range(T):
        w, s = map(int, sys.stdin.readline().split())
        W.append(w)
        S.app