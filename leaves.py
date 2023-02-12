"""
The function leaf_count calculates the amount of leaves in a binary tree recursively.
The input is the binary tree given as a namedtuple object.
The binary tree can include up to 100 nodes for the algorithm to work efficiently.
"""

from collections import namedtuple

def leaf_count(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1 
    return leaf_count(node.right) + leaf_count(node.left)
       

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    tree2 = Node(
    Node(Node(None,None),Node(None,None)),
    Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2
    print(count(tree2)) # 4
  
