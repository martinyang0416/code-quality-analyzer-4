import sys

MOD = 10**9 + 7

def main():
    Q = int(sys.stdin.readline())
    for _ in range(Q):
        M = int(sys.stdin.readline())
        B = list(map(int, sys.stdin.readline().split()))
        
        existing_dests = set()
        dest_freq = {}
        invalid = False
        
        for idx in range(M):
            val = B[idx]
            if val != 0:
                player = idx + 1
                if val == player:
                    invalid = True
                if val < 1 or 