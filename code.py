class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = [None, None]  # 0 and 1

class Trie:
    def __init__(self, C):
        self.root = TrieNode()
        self.C = C

    def insert(self, num):
        node = self.root
        for i in range(self.C-1, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def get_max_xor(self, num):
       