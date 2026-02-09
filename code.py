import sys

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in reversed(s):
            mask = (mask << 1) | (1 if c == 'H' else 0)
        masks.append(mask)
    
    # Build the trie
    trie = [ [None, None] ]  # root is node 0
    
    for mask in masks:
        current_node = 0
        for i in range(C-1, -1, -1):
            current_bit = (mask >> i) & 1
            c