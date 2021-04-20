# In-order Traversal for binary tree

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node=None):
        self.root = node

    def in_order_traversal(self, root):        
        # left, root, right
        #      60
        #   50   40
        # 30 20 10 1
        stack = []
        curr = root
        while curr != None or stack != []:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            if curr == None:
                curr = stack.pop()
                print(curr.val, end=" ")
                curr = curr.right


    def in_order_traversal_recurse(self, node):
        # left, root, child
        # visit left subtree
        # visit root
        # visit right subtree
        if node != None:
            self.in_order_traversal_recurse(node.left)
            print(node.val, end=" ")
            self.in_order_traversal_recurse(node.right)

    def pre_order_traversal(self, root):
        # root, left, right
        #      60
        #   50   40
        # 30 20 10 1
        #
        # 60 50 30 20 40 10 1
        stack = []
        curr = root
        while curr != None or stack != []:
            if curr != None:
                print(curr.val, end=" ")
                stack.append(curr)
                curr = curr.left
            if curr == None:
                curr = stack.pop()
                curr = curr.right

    def pre_order_traversal_recurse(self, node):
        # root, left, right
        #      60
        #   50   40
        # 30 20 10 1
        #
        # 60 50 30 20 40 10 1
        # visit root
        # recruse left subtree
        # recurse right subtree
        if node != None:
            print(node.val, end=" ")
            self.pre_order_traversal_recurse(node.left)
            self.pre_order_traversal_recurse(node.right)

    def post_order_traversal(self, root):
        # left, right, root
        #      60
        #   50   40
        # 30 20 10 1
        #
        # 30 20 50 10 1 40 60
        curr = root
        stack = []
        rs = []
        while curr != None or stack != []:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            if curr == None:
                curr = stack.pop()
                if curr.right == None or (rs != [] and rs[-1] == curr):
                    print(curr.val, end=" ")
                    if (rs != [] and rs[-1] == curr):
                        rs.pop()
                        curr = None
                        continue
                else:
                    stack.append(curr)
                    rs.append(curr)
                curr = curr.right

    def post_order_traversal_recurse(self, node):
        # left, right, root
        #      60
        #   50   40
        # 30 20 10 1
        #
        # 30 20 50 10 1 40 60
        # visit left subtree
        # visit right subtree
        # visit root
        if node != None:
            self.post_order_traversal_recurse(node.left)
            self.post_order_traversal_recurse(node.right)
            print(node.val)

if __name__ == "__main__":
    n1 = Node(60)
    n1.left = Node(50)
    n1.right = Node(40)
    n1.left.left = Node(30)
    n1.left.right = Node(20)
    n1.right.left = Node(10)
    n1.right.right = Node(1)
    t = Tree(n1)
    t.in_order_traversal(n1)
    print()
    t.in_order_traversal_recurse(n1)
    print()
    t.pre_order_traversal(n1)
    print()
    t.pre_order_traversal_recurse(n1)
    print()
    t.post_order_traversal(n1)
    print()