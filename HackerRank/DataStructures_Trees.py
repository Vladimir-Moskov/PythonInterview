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
# https://www.hackerrank.com/challenges/swap-nodes-algo/problem
# Swap Nodes [Algo]

def SwapNodesSolution():
    from collections import deque, defaultdict

    class Node:
        def __init__(self, data, level):
            self.data = data
            self.level = level
            self.left = None
            self.right = None


    def tree_for_print(root):
        result = deque()
        tree_for_print_rec(root, result)
        return result

    def tree_for_print_rec(root, result):
        if root:
            tree_for_print_rec(root.left, result)
            result.append(root.data)
            tree_for_print_rec(root.right, result)

    def swapNodes(queries, indexes):
        tree_dic = {1: Node(1, 1)}
        level_dic = defaultdict(deque)
        level_dic[1].append(tree_dic[1])
        level = deque([tree_dic[1]])

        for left_val, right_val in queries:
            parent = level.popleft()
            if left_val != -1:
                parent.left = Node(left_val, parent.level + 1)
                level.append(parent.left)
                tree_dic[left_val] = parent.left
                level_dic[parent.left.level].append(parent.left)
            if right_val != -1:
                parent.right = Node(right_val, parent.level + 1)
                level.append(parent.right)
                tree_dic[right_val] = parent.right
                level_dic[parent.right.level].append(parent.right)
        result = []
        for level in indexes:
            current_level = level
            while level_dic[current_level]:
                for node in level_dic[current_level]:
                    node.left, node.right = node.right, node.left
                current_level += level

            result.append(list(tree_for_print(tree_dic[1])))
        return result

    # case 0
    queries = [[2, 3], [-1, -1], [-1, -1]]
    indexes = [1, 1]
    # 3 1 2
    # 2 1 3
    #print(swapNodes(queries, indexes)) #

    # case1.0
    queries = [[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]
    indexes = [2]
    # 4 2 1 5 3
    #print(swapNodes(queries, indexes))

    # case1.1
    # 14 8 5 9 2 4 13 7 12 1 3 10 15 6 17 11 16
    # 9 5 14 8 2 13 7 12 4 1 3 17 11 16 6 10 15
    queries = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1],
     [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    indexes = [2, 3]
    #print(swapNodes(queries, indexes))


    # case 2
    queries = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
    indexes = [2, 4]
    # 2 9 6 4 1 3 7 5 11 8 10
    # 2 6 9 4 1 3 7 5 10 8 11
    print(swapNodes(queries, indexes))

# ===============================================================
class Node:
    def __init__(self, d):
        self.data = d


def build_tree(indexes):
    f = lambda x: None if x == -1 else Node(x)
    children = [list(map(f, x)) for x in indexes]
    nodes = {n.data: n for n in filter(None, sum(children, []))}
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        nodes[idx + 1].left = child_pair[0]
        nodes[idx + 1].right = child_pair[1]
    return nodes[1]


def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.data
            curr = curr.right


def swapNodes(indexes, queries):
    root = build_tree(indexes)
    for k in queries:
        h = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % k == 0:
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            h += 1
        yield inorder(root)
# ===============================================================


############################################################################################
# https://www.hackerrank.com/challenges/no-prefix-set/problem
# No Prefix Set

import os

def no_prefix_set_alternative(data_list):
    result = []
    data_list.sort()
    for i in range(len(data_list) - 1):
        j = i + 1
        while j < len(data_list) and data_list[j].startswith(data_list[i]):
            result.append(data_list[j])
            j += 1
    if result:
        result.insert(0, "BAD SET")
    else:
        result.insert(0, "GOOD SET")
    return result


class ChNode:
    def __init__(self, data, parent, is_end=False):
        self.data = data
        self.child = {}
        self.is_end = is_end


def no_prefix_set(data_list):
    word_dic = ChNode(None, None)

    for current_str in data_list:
        current_node = word_dic
        for i in range(0, len(current_str)):
            ch_val = current_str[i]
            if ch_val in current_node.child:
                child_node = current_node.child[ch_val]
                if child_node.is_end:
                    return ["BAD SET", current_str]
                if i == len(current_str) - 1:
                    return ["BAD SET", current_str]
                    # for temp_str in data_list:
                    #     if temp_str.startswith(current_str):
                    #         return ["BAD SET", temp_str]
            else:
                child_node = ChNode(current_str[i], current_node, i == len(current_str) - 1)
                current_node.child[current_str[i]] = child_node
            current_node = child_node

    return ["GOOD SET"]


data_list = ["aab", "aac", "aacghgh", "aabghgh"]
# data_list = ["ggbdfdhaffhghbdh", "dcjaichjejgheiaie", "d"]
# print(no_prefix_set(data_list))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     Q = int(input())
#     data_list = [None] * Q
#     for i in range(Q):
#         data_list[i] = input()
#
#     result = no_prefix_set(data_list)
#     fptr.write('\n'.join(result))
#     fptr.write('\n')
#     fptr.close()

############################################################################################