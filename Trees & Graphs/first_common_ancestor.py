# First Common Ancestor - Design an algorithm and write code to find the first
# common ancestor of two nodes in a binary tree. Avoid storing additional nodes
# in a data structure. NOTE: This is not necessarily a binary search tree.

# examples
#           1
#       2       3
#    4     5  6    7
#   8       9        10
# 11 12  13
#      14 

# solution 1:
# 1. Do a DFS post-order and as you encounter a node, put that in the ancestor1
#    list. Build the ancestor1 list as you go back up recursion. Similarly build
#    ancestor2 list. Loop through the two lists and the first match you find is
#    the common ancestor. If no matches are found, no common ancestor exists. We
#    can do it without additional storage by simply using two boolean variables
#    (child1found and child2found).  When the two nodes are found these two
#    variables will be set to true and the first node you encounter where both
#    are true is the first common acestor

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    #           1
    #       2       3
    #    4     5  6    7
    #   8       9        10
    # 11 12  13
    #      14 
    def common_ancestor(self, root, node1, node2):
        if root == None or root == node1 or root == node2:
            return root
        else:
            return self.find_common(root, node1, node2)

    def find_common(self, root, node1, node2):
        node1_found = None
        node2_found = None
        if root == node1 or root == node2:
            return root
        else:            
            if root.left != None:
                node1_found = self.find_common(root.left, node1, node2)
            if root.right != None:                
                node2_found = self.find_common(root.right, node1, node2)

            if node1_found and node2_found:
                return root
            else:
                return node1_found if node1_found != None else node2_found

n0 = Node(1)
n0.left = Node(2)
n0.right = Node(3)
n0.left.left = Node(4)
n0.left.right = Node(5)
n0.right.left = Node(6)
n0.right.right = Node(7)
n0.left.left.left = Node(8)
n0.left.right.right = Node(9)
n0.right.right.right = Node(10)
n0.left.left.left.left = Node(11)
n0.left.left.left.right = Node(12)
n0.left.right.right.left = Node(13)
n0.left.right.right.left.left = Node(14)
b = BinaryTree(n0)
print(b.common_ancestor(n0, n0.left.left, n0.left.left.left).data) # 4
print(b.common_ancestor(n0, n0.right.right.right, n0.left.left.left.left).data) #1
print(b.common_ancestor(n0, n0.left.left.left, n0.left.right.right).data) #2
print(b.common_ancestor(n0, n0.left.left, n0.left.right.right.left.left).data) #2
print(b.common_ancestor(n0, n0.right.left, n0.right.right.right).data) #3