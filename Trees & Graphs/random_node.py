# Random Node - You are implementing a binary tree class from scratch which, in
# addition to insert, find, and delete, has a method getRandomNode() which
# returns a random node from the tree. All nodes should be equally likely to be
# chosen. Design and implement an algorithm for getRandomNode, and explain how
# you would implement the rest of the methods.


# Example
#               10
#           20      12
#       90         8  4
#      6  2       1
#     7
#    1
#   8  2
#        3

# solutions
# 1. you can maintain a complete binary tree and get away with using an array
#    for all operations
# 2. you can calculate tree size, left subtree size at root and right subtree
#    size of root and store in root. Use this to define the probabilities of
#    picking a root, left or right nodes for your random node. Insert - do a bfs
#    and pick the first empty spot to plug in the node. find is bfs. delete is
#    find and use leaf to switch to delete node and adjust parent nodes pointers

# root has tree size, left subtree size and right subtree size. Generate a
# random number between 1 and tree_size. If it's 1, pick root, if it's < left
# tree size, go left, else go right. recurse and repeat

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1

class BinartyTree:
    def __init__(self, root=None):
        self.root = root
        self.last_leaf = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            curr = self.root
            while True:
                curr.size += 1
                if data <= curr.data:
                    if not curr.left:
                        curr.left = new_node
                        break
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = new_node
                        break
                    curr = curr.right                

    def delete(self, data):
        pass

    def find(self, data):
        pass

    def get_random_node(self):
        curr = self.root
        while True:
            rand = random.randint(1, curr.size)
            if rand == curr.size:
                return curr.data
            elif rand < curr.left.size + 1:
                curr = curr.left
            else:
                curr = curr.right

    def __str__(self, root=-1, lvl=0):
        if root == -1:
            root = self.root
        ret = "\t" * lvl + "Data: " + str(root.data) + ", Size: " + str(root.size) + "\n"
        if root.left != None:
            ret += self.__str__(root.left, lvl+1)
        if root.right != None:
            ret += self.__str__(root.right, lvl+1)
        return ret

b = BinartyTree()
b.insert(10)
b.insert(20)
b.insert(12)
b.insert(90)
b.insert(8)
b.insert(4)
b.insert(2)
b.insert(21)
print(b)
print(b.get_random_node())