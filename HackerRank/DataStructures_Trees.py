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
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?h_r=next-challenge&h_v=legacy
# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
# Binary Search Tree : Insertion
# Tree: Preorder Traversal

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val, currentNode=None):
        if not self.root:
            self.root = Node(val)
            return
        if not currentNode:
            currentNode = self.root
        if currentNode.info < val:
            if not currentNode.right:
                currentNode.right = Node(val)
            else:
                self.insert(val, currentNode.right)
        else:
            if not currentNode.left:
                currentNode.left = Node(val)
            else:
                self.insert(val, currentNode.left)

############################################################################################
# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
# Binary Search Tree : Lowest Common Ancestor

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''

def search(root, value):
    result = [root]
    current = root
    while current:
        result.append(current)
        if current.info == value:
            return result
        else:
            if current.info > value:
                current = current.left
            else:
                current = current.right
    else:
        return []


def lca_bad(root, v1, v2):
    path1 = search(root, v1)
    path2 = search(root, v2)

    i = 0
    while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
        i += 1
    return path1[i - 1]

# optimal solution
def lca(root, v1, v2):
    current = root
    while current:
        if current.info == v1 or current.info == v2:
            return current
        else:
            if current.info > v1 and current.info > v2:
                current = current.left
            elif current.info < v1 and current.info < v2:
                current = current.right
            else:
                return current
############################################################################################
