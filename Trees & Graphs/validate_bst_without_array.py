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
# 1. do an in-order dfs traversal and make sure the numbers are in ascending sorted order - O(n)
# 2. get all the elements in the left tree for a node and all elements in right
#    substree for a node and make sure all left elements <= node < all right
#    elements. Repeat this exercise for each node O(n * n) 
#    n-1, 2*(n-3), 4*(n-7)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def is_bst(self, root):
        return self.in_order_traversal(root)

    def in_order_traversal(self, root, prev=[None]):
        if root == None:
            return True
        else:
            if not self.in_order_traversal(root.left, prev):
                return False
            if prev[0] != None and prev[0] > root.data:
                return False
            prev[0] = root.data
            if not self.in_order_traversal(root.right, prev):
                return False
            return True

n0 = Node(10)
n0.left = Node(4)
n0.right = Node(17)
n0.left.left = Node(3)
n0.left.right = Node(11)
b = BinaryTree(n0)
print(b.is_bst(n0))