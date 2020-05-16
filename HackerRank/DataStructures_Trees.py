############################################################################################
# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
# Tree: Level Order Traversal

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque


def levelOrder(root):
    result = deque([root])
    index = 0
    while index < len(result):
        if result[index].left:
            result.append(result[index].left)
        if result[index].right:
            result.append(result[index].right)
        index += 1

    print(" ".join(map(lambda x: str(x.info), result)))

############################################################################################

