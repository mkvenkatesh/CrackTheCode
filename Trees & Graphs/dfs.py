# DFS

class Node:
    def __init__(self, value=None):
        self.value = value
        self.visited = False
        self.children = []

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

class DFS:
    def search(self, node):
        if not node.visited:
            print(node.value)
            node.visited = True
            for child in node.children:
                if not child.visited:
                    self.search(child)

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n0.children = [n1, n4, n5]
n1.children = [n3, n4]
n2.children = [n1]
n3.children = [n2, n4]
DFS().search(n0)