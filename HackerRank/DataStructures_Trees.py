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
# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
# Tree: Inorder Traversal

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import deque


def inOrder(root):
    result = inOrderRecursive(root, [])
    print(" ".join(map(str, result)))


def inOrderRecursive(root, result):
    if root:
        result = inOrderRecursive(root.left, result) + [root] + inOrderRecursive(root.right, result)
    return result

############################################################################################
# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
#

from collections import deque


def postOrderIterative(root):
    result = [root]
    current_q = deque([root])
    while current_q:
        next_q = []
        while current_q:
            next_node = current_q.pop()
            if next_node.left:
                next_q.append(next_node.left)
            if next_node.right:
                next_q.append(next_node.right)

        reversed(next_q)
        result = next_q + result
        current_q = deque(next_q)

    print(" ".join(map(lambda x: str(x.info), result)))

def postOrder(root):
    #Write your code here

    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")

############################################################################################
