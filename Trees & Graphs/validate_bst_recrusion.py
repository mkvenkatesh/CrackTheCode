# Implement a function to check if a binary tree is a binary search tree.

# example 1
#       10
#   4       17
# 3   5   11  18

# example 2
#       10
#   4       17
# 3   5   6   18

# solution
# 1. maintain two vars - MIN and MAX that you keep updating as you traverse down
#    the tree. Moving to the left, update Max var and moving to the right update
#    MIN var. Compare this min and max with the node value as you visit each
#    node. If the node value is between min and max, return True else false

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def is_bst(self, root, min_val=None, max_val=None):
        if root == None:
            return True
        else:
            if not self.is_bst(root.left, min_val, root.data):
                return False

            if not self.is_bst(root.right, root.data, max_val):
                return False

            if min_val == None and max_val == None:                
                return True
            elif min_val == None and root.data < max_val:
                return True
            elif max_val == None and min_val <= root.data:
                return True
            elif min_val <= root.data < max_val:
                return True
            else:
                return False
            

n0 = Node(10)
n0.left = Node(4)
n0.right = Node(17)
n0.left.left = Node(3)
n0.left.right = Node(11)
b = BinaryTree(n0)
print(b.is_bst(n0))