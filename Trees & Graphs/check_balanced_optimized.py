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
#
# calculate the height of the left subtree and right subtree along with if the
# tree is balanced at that node or not and use recursion to visit all the nodes
# by returning these two values properly

from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def is_balanced(self, node):
        if node == None:
            return (0, True)
        else:
            left_info = self.is_balanced(node.left)
            right_info = self.is_balanced(node.right)
            left_height = left_info[0]
            right_height = right_info[0]
            left_balanced = left_info[1]
            right_balanced = right_info[1]
            node_height = max(left_height, right_height) + 1
            if (abs(left_height - right_height) > 1) or left_balanced == False or right_balanced == False:
                return (node_height, False)
            else:
                return (node_height, True)



#             9
#        8           7
#    6       5   1       8
#   1 4     4 6 6 2     1 
#              1        
n0 = Node(9)
n0.left = Node(8)
n0.right = Node(7)
n0.left.left = Node(6)
# n0.left.right = Node(5)
n0.right.left = Node(1)
n0.right.right = Node(8)
n0.left.left.left = Node(1)
n0.left.left.right = Node(4)
# n0.left.right.left = Node(4)
# n0.left.right.right = Node(6)
n0.right.left.left = Node(6)
n0.right.left.right = Node(2)
n0.right.right.left = Node(1)
n0.right.right.right = Node(0)
#n0.left.right.right.right = Node(1)

b = BinaryTree(n0)
print("Balanced Tree: ", b.is_balanced(n0))