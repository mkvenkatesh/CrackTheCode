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

# after (incoming)
# d -> a,b
# b -> f
# a -> f
# c -> d

# before (outgoing)
# a -> d
# f -> b,a
# b -> d
# d -> c
# e -> 
# c -> 

# solutions
# 1. parse through dependency list to build two hash tables, one is depends on
#    and other is reverse. Missing project keys in depends-on list go to the
#    output. For each output, check reverse depends on to see what other
#    projects can be added to output. Proceed like this for each added output.

class BuildOrder:
    def build_order(self, projects, dependencies):
        after_dict = {}
        before_dict = {}
        output = []
        for d in dependencies:
            if d[0] not in before_dict:
                before_dict[d[0]] = [d[1]]
            else:
                before_dict[d[0]].append(d[1])
            
            if d[1] not in after_dict:
                after_dict[d[1]] = [d[0]]
            else:
                after_dict[d[1]].append(d[0])

        for project in projects:
            if project not in after_dict:
                output.append(project)

        for o in output:
            if o in before_dict:
                for v in before_dict[o]:
                    for k in after_dict[v]:
                        if k in output and v not in output:
                            output.append(v)

        if len(output) == len(projects):
            return output
        else:
            return "No build order found"

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

b = BuildOrder()
print(b.build_order(projects, dependencies))