# Given a min or max heap as array, build a tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class HeapTree:
    def __init__(self):
        self.root = None
    
    def build_tree(self, heap_array):
        i = 0
        self.root = Node(heap_array[0])
        stack = [self.root]
        for node in stack:
            left_idx = (2 * i) + 1
            right_idx = (2 * i) + 2
            if left_idx < len(heap_array):
                node.left = Node(heap_array[left_idx])
                stack.append(node.left)
            if right_idx < len(heap_array):
                node.right = Node(heap_array[right_idx])
                stack.append(node.right)
            i += 1
            
    def build_tree_recurse(self, heap_array, i=0, curr=None):  
        if i >= len(heap_array):
            return
        else:
            if not self.root:
                self.root = Node(heap_array[0])
                curr = self.root
            if ((2*i) + 1) < len(heap_array):
                curr.left = Node(heap_array[(2*i) + 1])
                self.build_tree_recurse(heap_array, (2*i)+1, curr.left)
            if ((2*i) + 2) < len(heap_array):
                curr.right = Node(heap_array[(2*i) + 2])
                self.build_tree_recurse(heap_array, (2*i)+2, curr.right)


    # def __str__(self, curr=0, level=0, print_str=[]):
    #     if curr == None:
    #         return print_str
    #     else:
    #         if level == 0:
    #             curr = self.root
    #             print_str.append(str(curr.value))
    #             level += 1
    #         if curr.left != None:
    #             print_str.append("\n" + level*"  " + "-" + str(curr.left.value))
    #             print_str = self.__str__(curr.left, level+1)
    #         if curr.right != None:
    #             print_str.append("\n" + level*"  " + "-" + str(curr.right.value))            
    #             print_str = self.__str__(curr.right, level+1)
    #     if level == 1:
    #         return "".join(print_str)
    #     else:
    #         return print_str

    def __str__(self, curr=-1, level=0):
        if curr == -1:
            curr = self.root
        ret = (level * "\t") + str(curr.value) + "\n"
        if curr.left != None:
            ret += self.__str__(curr.left, level+1)
        if curr.right != None:
            ret += self.__str__(curr.right, level+1)
        return ret

heap_array = [4, 50, 7, 55, 90, 87]
h = HeapTree()
# h.build_tree(heap_array)
h.build_tree_recurse(heap_array)
print(h)
