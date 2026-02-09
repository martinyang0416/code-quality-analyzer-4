import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        K = int(input[ptr+1])
        ptr +=2
        A = list(map(int, input[ptr:ptr+K]))
        ptr += K
        m = max(A)
        if N >= m:
            print(0)
        else:
            res = 1
            for i in range(1, N+1):
                res = (res * i) % m
            print(res % m)
            
if __name__ == "__main__":