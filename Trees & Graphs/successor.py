# Successor - Write an algorithm to find the "next" node (i.e., in-order
# successor) of a given node in a binary search tree. You may assume that each
# node has a link to its parent.

# examples
#        10
#   5           15
# 2   6      11    21

# solutions
# 1. do in-order traversal and store that in an array and scan through the
#    elements to find the given node and get the next node in the array
# 2. do in-order traversal until you hit the given node and on your next visit
#    to a node, return that node
# 3. Given a node, the next node is always going to be to the right side of the
#    tree to the given nodes. There are few scenarios 
#    a) given a node, if left and right child are none, go to parent and see if
#    the node is the left of the parent. If so, get the parent value for 'next'
#    node.
#    b) given a node, if left and right child are none, go to parent and see if
#    node is right of parent. If so,  go to parent's parent to get the next node
#    value
#    c) given a node, if it has a right child, go all the way to the left of it
#    to get the next node

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def successor(self, node):
        if node.right == None:
            parent = node.parent
            if parent.left == node:
                return parent.data
            else:
                while parent != None and parent.left != node:
                    node = parent
                    parent = parent.parent
                if parent == None:
                    return None
                else:
                    return parent.data
        elif node.right != None:
            node = node.right
            while node.left != None:
                node = node.left
            return node.data

n0 = Node(10)

n0.left = Node(5, n0)
n0.right = Node(15, n0)

n0.left.left = Node(2, n0.left)
n0.left.right = Node(6, n0.left)

n0.right.left = Node(11, n0.right)
n0.right.right = Node(21, n0.right)

n0.left.left.right = Node(3, n0.left.left)
n0.left.right.right = Node(7, n0.left.right)


b = BST(n0)
print(b.successor(n0.left.right.right))
print(b.successor(n0.right.right))