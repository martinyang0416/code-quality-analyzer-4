import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        rows = int(input[ptr])
        cols = int(input[ptr+1])
        start_r = int(input[ptr+2])
        start_c = int(input[ptr+3])
        ptr +=4
        
        k = int(input[ptr])
        ptr +=1
        
        closed = set()
        for __ in range(k):
            r = int(input[ptr])
            c = int(input[ptr+1])
      