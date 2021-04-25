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
        in_order_elements = self.in_order_traversal(root)
        print(in_order_elements)
        if(self.check_ascending(in_order_elements)):
            return True
        else:
            return False

    def in_order_traversal(self, root, elements=[]):
        if root == None:
            return []
        else:
            self.in_order_traversal(root.left, elements)
            elements += [root.data]
            self.in_order_traversal(root.right, elements)
            return elements

    def check_ascending(self, in_order_elements):
        for i in range(len(in_order_elements)-1):
            if in_order_elements[i] > in_order_elements[i+1]:
                return False
        return True

n0 = Node(10)
n0.left = Node(4)
n0.right = Node(17)
n0.left.left = Node(3)
n0.left.right = Node(9)
b = BinaryTree(n0)
print(b.is_bst(n0))