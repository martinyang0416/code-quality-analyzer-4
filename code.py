import heapq
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr]); ptr +=1
    M = int(input[ptr]); ptr +=1
    E = int(input[ptr]); ptr +=1
    S = int(input[ptr]); ptr +=1
    T = int(input[ptr]); ptr +=1
    R = int(input[ptr]); ptr +=1

    original_roads = []
    for _ in range(M):
        a = int(input[ptr]); ptr +=1
        b = int(input[ptr]); ptr +=1
        original_roads.append((a, b))
    
    events 