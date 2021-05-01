# Check Subtree - T1 and T2 are two very large binary trees, with T1 much bigger
# than T2. Create an algorithm to determine if T2 is a subtree of Tl. A tree T2
# is a subtree of Tl if there exists a node n in T1 such that the subtree of n
# is identical to T2. That is, if you cut off the tree at node n, the two trees
# would be identical.

# exampes
#           T1
#          90
#      8       7
#   6    8   9  21
# 1       7 8 10  90

#           T2
#          7
#      9       21
#     8 10       90

# solutions
# 1. generate all subtrees of all nodes in t1. compare the subtree array with t2
#    to see if there are any matches
# 2. Generate dfs pre-order for T1 and T2 but also store if the node is
#    a leaf or non-leaf node. now compare t2 array to t1 array on both
#    leaf/non-leaf property and the value.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def dfs_preorder(self, root, dfs_list=[]):
        if root != None:
            if root.left == None and root.right == None:
                dfs_list.append((root.data, 1))
            else:
                dfs_list.append((root.data, 0))            
            self.dfs_preorder(root.left, dfs_list)
            self.dfs_preorder(root.right, dfs_list)
        return dfs_list

    def is_subtree(self, larger_tree):
        t1 = self.dfs_preorder(larger_tree.root, [])
        t2 = self.dfs_preorder(self.root, [])
        ptr_t1 = 0
        ptr_t2 = 0
        while True:
            if (t1[ptr_t1][0] == t2[ptr_t2][0]) and (t1[ptr_t1][1] == t2[ptr_t2][1]):
                ptr_t1 += 1
                ptr_t2 += 1
            else:
                ptr_t1 += 1
                ptr_t2 = 0
            
            if ptr_t2 == len(t2):
                return True
            
            if ptr_t2 == 0 and ptr_t1 > len(t1) - len(t2):
                return False

#           T1
#          90
#      8       7
#   6    8   9  21
# 1       7 8 10  90
n0 = Node(90)
n0.left = Node(8)
n0.right = Node(7)
n0.left.left = Node(6)
n0.left.right = Node(8)
n0.right.left = Node(9)
n0.right.right = Node(21)
n0.left.left.left = Node(1)
n0.left.right.right = Node(7)
n0.right.left.left = Node(8)
n0.right.left.right = Node(10)
n0.right.right.right = Node(90)


t1 = BinaryTree(n0)

#           T2
#          7
#      9       21
#     8 10       90
n1 = Node(7)
n1.left = Node(9)
n1.right = Node(21)
n1.left.left = Node(8)
n1.left.right = Node(10)
n1.right.right = Node(90)

t2 = BinaryTree(n1)

print(t2.is_subtree(t1))

