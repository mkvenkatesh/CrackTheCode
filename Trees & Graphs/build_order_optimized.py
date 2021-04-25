# Build Order - You are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is dependent
# on the first project). All of a project's dependencies must be built before
# the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.

# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
# Output: f, e, a, b, d, c

# before (outgoing)
# a -> d
# f -> b,a
# b -> d
# d -> c
# e -> 
# c -> 

# solutions
# 1. build a hash table with project node as key and the edge as values (a->b),
#    a is the key and b is dependent on a to complete. Maintain an incoming
#    links for each project node as well. Incoming links of 0 nodes can be added
#    to output. Loop through output and decrement incoming nodes for each
#    dependent nodes on output and add them to output if incoming is 0.

class BuildOrder:
    def build_order(self, projects, dependencies):
        dependency_graph = {}
        incoming_count = {}
        output = []

        for project in projects:
            incoming_count[project] = 0
            dependency_graph[project] = []

        for d in dependencies:
            dependency_graph[d[0]].append(d[1])            
            incoming_count[d[1]] += 1
        
        for item in incoming_count.items():
            if item[1] == 0:
                output.append(item[0])
        
        if output == []:
            return "No build order found"

        for o in output:
            for v in dependency_graph[o]:
                incoming_count[v] -= 1
                if incoming_count[v] == 0:
                    output.append(v)

        return output


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

b = BuildOrder()
print(b.build_order(projects, dependencies))