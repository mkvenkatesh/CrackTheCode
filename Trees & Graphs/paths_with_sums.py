# Paths with Sum - You are given a binary tree in which each node contains an
# integer value (which might be positive or negative). Design an algorithm to
# count the number of paths that sum to a given value. The path does not need to
# start or end at the root or a leaf, but it must go downwards (traveling only
# from parent nodes to child nodes).

# examples
#           -10
#       2           8
#   6      -1   -4     5
#  3                 -1  5  
# 3                        -6  
#                         2

# Given value: 4
# output: 
#   [-10, 2, 6, 3, 3]
#   [8, -4]
#   [5, -1]
#   [5, 5, -6]
#   [-10, 8, 5, 5, -6, 2]

# solutions
# 1. start dfs from each node in the tree and do cumulative sum of the path
#    values until you hit leaf, if you sum up to the given value during this
#    path increment the counter - O(n^2)
# 2. as you do dfs from root, pass the current node element to recursively and
#    sum parent and child node and append it to an an array.

#   -10: []
#   2:   [-8]
#   6:   [-2, 8]
#   3:   [1, 11, 9]
#   3:   [4, 14, 12, 6]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def paths_with_sum(self, root, value, parent_data=None, path_sums=[], paths_found=0):
        if root == None:
            return paths_found
        else:
            sum_array = list(map(lambda x: x + root.data, path_sums))
            if parent_data:
                sum_array.append(parent_data + root.data)
            paths_found += sum_array.count(value)
            paths_found = self.paths_with_sum(root.left, value, root.data, sum_array, paths_found)
            paths_found = self.paths_with_sum(root.right, value, root.data, sum_array, paths_found)

        return paths_found

#           -10
#       2           8
#   6      -1   -4     5
#  3                 -1  5  
# 3                        -6  
#                         2

n0 = Node(-10)
n0.left = Node(2)
n0.right = Node(8)
n0.left.left = Node(6)
n0.left.right = Node(-1)
n0.left.left.left = Node(3)
n0.left.left.left.left = Node(3)
n0.right.left = Node(-4)
n0.right.right = Node(5)
n0.right.right.left = Node(-1)
n0.right.right.right = Node(5)
n0.right.right.right.right = Node(-6)
n0.right.right.right.right.left = Node(2)

b = BinaryTree(n0)
print(b.paths_with_sum(n0, 4))