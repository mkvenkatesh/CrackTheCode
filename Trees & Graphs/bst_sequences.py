# BST Sequences - A binary search tree was created by traversing through an
# array from left to right and inserting each element. Given a binary search
# tree with distinct elements, print all possible arrays that could have led to
# this tree.

# Input:  2
#        /\
#       1  3
# Output: {2, 1, 3}, {2, 3, 1}

# Input
#              20
#       10          30
#     5   15      25
# {20, 10, 30, 5, 15, 25}, {20, 10, 30, 15, 5, 25}, {20, 30, 10, 5, 15, 25}, {20, 30, 10, 15, 5, 25}
# {20, 10, 30, 25, 5, 15}, {20, 10, 30, 25, 15, 5}, {20, 30, 10, 5, 25, 15}, {20, 30, 10, 15, 25, 5}
# {20, 10, 30, 5, 25, 15}, {20, 10, 30, 15, 25, 5}, {20, 30, 10, 25, 5, 15}, {20, 30, 10, 25, 15, 5}
# l0! * l1! * l2!

# solutions 

# 1. do bfs and store all the level nodes in array of arrays. loop through this
#    array and create all permutations of the array, go to next one create
#    permutations and append to all the previous ones. Rinse and repeat

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def bst_sequences(self):
        if self.root == None:
            return None
        
        levels = self.get_level_array_bfs(self.root)
        for l in levels:
            for i in range(len(l)):
                l[i] = l[i].data

        for i in range(len(levels)):
            levels[i] = self.permutate(levels[i], [], [])
        
        bst_seqs = []
        temp_seqs = []
        for lvl in levels:
            for perm in lvl:
                if bst_seqs == []:
                    temp_seqs.append(perm)
                else:
                    for seq in bst_seqs:
                        temp_seqs.append(seq+perm)
            bst_seqs = temp_seqs
            temp_seqs = []

        return bst_seqs

    def permutate(self, lvl_array, prefix=[], perm_arr=[]):
        if lvl_array == []:
            perm_arr.append(prefix[:])
            return perm_arr
        else:
            for i in range(len(lvl_array)):
                prefix.append(lvl_array[i])
                self.permutate(lvl_array[:i] + lvl_array[i+1:], prefix, perm_arr)
                prefix.pop()
            return perm_arr

    def get_level_array_bfs(self, root):
        level_array = [[root]]
        for level in level_array:
            next_level_nodes = []
            for node in level:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            if next_level_nodes:
                level_array.append(next_level_nodes)
        return level_array


    def __str__(self, node=-1, lvl=0):    
        if node == -1:
            node = self.root
        ret = "\t" * lvl + str(node.data) + "\n"
        if node.left != None:
            ret += self.__str__(node.left, lvl+1)
        if node.right != None:
            ret += self.__str__(node.right, lvl+1)
        return ret

n0 = Node(20)
n0.left = Node(10)
n0.right = Node(30)
n0.left.left = Node(5)
n0.left.right = Node(15)
n0.right.left = Node(25)
n0.right.right = Node(35)

b = BST(n0)
# print(b)
ret = b.bst_sequences()
print(len(ret))
print()
print(ret)