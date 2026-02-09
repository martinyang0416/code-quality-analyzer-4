import sys

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sorted_li = []
        self.prefix_max = []

def build_tree(ropes, start, end):
    node = SegmentTreeNode(start, end)
    if start == end:
        li, ri = ropes[start]
        node.sorted_li = [(li, ri)]
        node.prefix_max = [ri]
    else:
        mid = (start + end) // 2
        node.left = build_tree(rope