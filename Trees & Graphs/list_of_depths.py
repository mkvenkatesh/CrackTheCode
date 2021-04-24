# List of Depths: Given a binary tree, design an algorithm which creates a
# linked list of all the nodes at each depth (e.g., if you have a tree with
# depth D, you'll have D linked lists).

# examples
#          9
#      8       7
#   1    2  4
#  0  7 8  9  9
#               5

# solutions
# 1. use bfs
#   ll_queue < add root 
#   for each ll in stack:
#       add all children of node to stack

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:            
            self.head, new_node.next = new_node, self.head            

    def __str__(self):
        curr = self.head
        ret = []
        while curr != None:
            ret.append(str(curr.data.data))
            curr = curr.next
        return " ".join(ret)

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def list_of_depths(self):
        ll = LinkedList()
        ll.add(self.root)
        q = [ll]
        for linkedlist in q:
            curr = linkedlist.head
            ll = LinkedList()
            while curr != None:
                if curr.data.left != None:
                    ll.add(curr.data.left)
                if curr.data.right != None:
                    ll.add(curr.data.right)
                curr = curr.next
            if ll.head != None:
                q.append(ll)
        return q

n0 = TreeNode(9)
n0.left = TreeNode(8)
n0.right = TreeNode(7)
n0.left.left = TreeNode(1)
n0.left.right = TreeNode(2)
n0.right.left = TreeNode(4)
n0.left.left.left = TreeNode(0)
n0.left.left.right = TreeNode(7)
n0.left.right.left = TreeNode(8)
n0.left.right.right = TreeNode(9)
n0.right.left.right = TreeNode(9)
b = BinaryTree(n0)
q = b.list_of_depths()

for ll  in q:
    print(ll)