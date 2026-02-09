import bisect
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = int(input[ptr]), int(input[ptr+1])
        ptr +=2
        s = input[ptr]
        ptr +=1
        p = list(map(int, input[ptr:ptr+m]))
        ptr +=m
        p.sort()
        counts = [0]*26
        for i in range(n):
            x = i + 1
            idx = bisect.bisect_left(p, x)
            cnt_p = m - idx
            total = cnt_p 