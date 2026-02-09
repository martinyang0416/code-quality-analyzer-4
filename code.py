import sys

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask = (mask << 1) | (1 if c == 'H' else 0)
        masks.append(mask)

    # Build the trie as a list of dictionaries
    nodes = [{'0': None, '1': None}]  # root is node 0

    for mask in masks:
        node_id = 0
        for i in range(C-1, -1, -1):
            bit = (mask >> i) & 1
         