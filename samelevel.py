"""
The function leaf_count_level() calculates the amount of nodes on certain level in a binary tree.
By level we mean that the root is on level 1, its children are on level 2 etc.
The function gets a binary tree and desired level as its input and computes the count of nodes 
on the level recursively. 
The tree can contain up to 100 nodes for the algorithm to work efficiently.
"""

from collections import namedtuple

def leaf_count_level(node, level):
    if level == 1 and node:
        return 1
    if not node:
        return 0
    return leaf_count_level(node.left, level-1) + leaf_count_level(node.right, level-1)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(leaf_count_level(tree,1)) # 1
    print(leaf_count_level(tree,2)) # 1
    print(leaf_count_level(tree,3)) # 2
    print(leaf_count_level(tree,4)) # 0
    
