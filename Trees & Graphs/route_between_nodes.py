# Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

# questions
# Does it mean if node1 has a path to node2 or node2 has a path to node1, the
# condition is true?

# examples

 # a-> b, c, d
 # b -> e, f
 # f -> g

# solutions
# 1. bfs on node1 and bfs on node2 to confirm if a route is there, since it's a
#    directed graph. If it's undirected, we could've done bi-directional BFS
#    search.

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.children = []

class RouteExistsNodes:
    def search_route(self, node1, node2):
        if (node1 == node2) or (self.bfs(node1, node2) or self.bfs(node2, node1)):
            return True
        else:
            return False
 
    def bfs(self, start, end):
        q = [start]
        for node in q:
            if not node.visited:
                if node == end:
                    return True
                node.visited = True
                if node.children != []:
                    q += node.children
        # clear all the visited values for second round
        for node in q:
            node.visited = False
        return False

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
print(RouteExistsNodes().search_route(n0, n5))
print(RouteExistsNodes().search_route(n1, n5))