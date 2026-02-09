import collections

def validateBinaryTreeNodes(n, leftChild, rightChild):
    # Check if any node has the same non-null left and right child
    for i in range(n):
        if leftChild[i] != -1 and leftChild[i] == rightChild[i]:
            return False
    
    # Collect all child nodes to determine the root
    children = set()
    for i in range(n):
        l, r = leftChild[i], rightChild[i]
        if l != -1:
            children.add(l)
        if r != -1:
            children.add(r)
    
