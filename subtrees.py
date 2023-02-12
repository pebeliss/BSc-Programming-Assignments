"""
These functions calculate the largest difference in node count between some subtrees of given binary tree.
The difference() function gets the binary tree as its input, keeps count of the largest difference and outputs it.
The leaf_count_diff() function calculates the actual differences recursively.
"""

from collections import namedtuple

def leaf_count_diff(node):
    if not node:
        return 0
    return leaf_count_diff(node.left) + leaf_count_diff(node.right) + 1

def difference(node):
    if not node:
        return 0
    max_Value = abs(leaf_count_diff(node.left) - leaf_count_diff(node.right))
    return max(difference(node.left), difference(node.right), max_Value)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(difference(tree)) # 3
