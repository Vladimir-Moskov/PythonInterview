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
# https://www.hackerrank.com/challenges/tree-top-view/problem
# Tree : Top View


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque
def topView(root):
    if (root == None):
        return
    q = deque()
    m = {}
    hd = 0
    root.hd = hd

    # push node and horizontal
    # distance to queue
    q.append(root)

    while len(q):
        root = q[0]
        hd = root.hd

        # count function returns 1 if the
        # container contains an element
        # whose key is equivalent to hd,
        # or returns zero otherwise.
        if hd not in m:
            m[hd] = root.info
        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)

        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)

        q.popleft()

    print(" ".join(map(lambda x: str(m[x]), sorted(m))))

############################################################################################
