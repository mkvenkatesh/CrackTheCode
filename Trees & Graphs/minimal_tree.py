# Minimal Tree - Given a sorted (increasing order) array with unique integer
# elements, write an algo­rithm to create a binary search tree with minimal
# height.

# examples
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# binary search tree
#           5
#       3           8
#   2       4   7       9
# 1           6

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# binary search tree
#           4
#       2
#   1

# solutions
# build a tree with binary search
# set root to mid
# set root's left to mid of 0 to mid
# set root's right to mid of mid to end
# recurse

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def build_bst_from_array(self, array, start, end):
        if start > end:
            return None
        else:
            mid = (start + end)//2
            new_node = Node(array[mid])
            if self.root == None:
                self.root = new_node
            new_node.left = self.build_bst_from_array(array, start, mid-1)
            new_node.right = self.build_bst_from_array(array, mid+1, end)
            return new_node

    def __str__(self, node=-1, level=0):
        if node == -1:
            node = self.root
        ret = (level * "\t") + str(node.value) + "\n"
        if node.left != None:
            ret += self.__str__(node.left, level+1)
        if node.right != None:
            ret += self.__str__(node.right, level+1)
        return ret

arr = [1, 2, 3, 4, 5, 6, 7]

b = BST()
b.build_bst_from_array(arr, 0, len(arr)-1)
print(b)
