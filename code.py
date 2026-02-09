import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        minScore = list(map(int, input[idx:idx+N]))
        idx += N
        scholarships = []
        for _ in range(M):
            r = int(input[idx])
            ma = int(input[idx+1])
            scholarships.append((r, ma, 0))
            idx += 2
        qual = []
        for _ in ran