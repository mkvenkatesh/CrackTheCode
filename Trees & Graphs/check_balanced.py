# check balanced - Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more
# than one.

# examples
#             9
#        8          7
#    6       5  1       8
#   1 4     4 6
#              1

# solutions
# 1. For each node, do dfs on left and right subtree and get the max level on each
# and compare the difference. If it's more than 1 for any node it's not balanced - O(n^2)

from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def get_level_by_bfs(self, node):
        if node != None:
            q = Queue()
            q.put((node,0))
            max_lvl = 0
            while not q.empty():
                popped_val = q.get()
                node = popped_val[0]
                depth = popped_val[1]
                if node.left != None:
                    q.put((node.left, depth+1))
                if node.right != None:
                    q.put((node.right, depth+1))
                if max_lvl < depth:
                    max_lvl = depth
            return max_lvl
        else:
            return 0

    def is_balanced(self, node):
        if node != None:
            left_depth = self.get_level_by_bfs(node.left)
            right_depth = self.get_level_by_bfs(node.right)
            if abs(left_depth - right_depth) > 1:
                return False
            if node.left != None:
                return self.is_balanced(node.left)
            if node.right != None:
                return self.is_balanced(node.right)
            
            return True
#             9
#        8           7
#    6       5   1       8
#   1 4     4 6 6 2     1 
#              1        
n0 = Node(9)
n0.left = Node(8)
n0.right = Node(7)
n0.left.left = Node(6)
n0.left.right = Node(5)
n0.right.left = Node(1)
n0.right.right = Node(8)
n0.left.left.left = Node(1)
n0.left.left.right = Node(4)
n0.left.right.left = Node(4)
n0.left.right.right = Node(6)
#n0.right.left.left = Node(6)
#n0.right.left.right = Node(2)
#n0.right.right.left = Node(1)
# n0.right.right.right = Node(0)
n0.left.right.right.right = Node(1)

b = BinaryTree(n0)
print("Balanced Tree: ", b.is_balanced(n0))