import sys

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    n, m = int(data[ptr]), int(data[ptr+1])
    ptr +=2
    a = list(map(int, data[ptr:ptr+n]))
    ptr +=n
    q = int(data[ptr])
    ptr +=1
    queries = [ (int(data[ptr+2*i])-1, int(data[ptr+2*i+1])-1) for i in range(q) ]

    # Compute prev array
    prev = [-1]*n
    last_occurrence = {}
    for i in range(n):
        if a[i] in last_occurrence:
            prev[i] = last_occurrence[a[i]]
        else