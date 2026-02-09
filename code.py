import sys

def main():
    n = int(sys.stdin.readline())
    matrix = []
    for _ in range(n):
        s = sys.stdin.readline().strip()
        row = []
        for c in s:
            binary = format(int(c, 16), '04b')
            row.extend([int(bit) for bit in binary])
        matrix.append(row)
    
    # Compute prefix sum matrix (integral image)
    integral = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += matr