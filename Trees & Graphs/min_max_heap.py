# Min-Heap & Max-Heap

# Min-heap is a complete binary tree (all the nodes are filled out and the leaf
# nodes are filled from left to right and each node can have atmost of 2 nodes)
# where each node's value is less than that of it's children. Max-heap is the
# opposite

# Two methods - Insert & Extract-Min.

# Insert a node is inserted as the right most node in the last level and then we
# perform heapify i.e. the node is swapped with it's ancestors based on value
# comparison.

# Extract-min is removing the root element and replacing that with the right
# most node in the leaf and performing a heapify i.e. swapping node value with
# ancestors to satisfy the min-heap property

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self, node=None):
        self.root = node
        self.last_node = None
        self.insert_node = None
    
    def insert(self, value):
        # last level is full, then insert node in leftmost node
        # last level is not full, then insert to left or right of the incomplete node
        new_node = Node(value)
        self.insert_node = self.get_node_insertion()        
        if self.insert_node.left == None:
            self.insert_node.left = new_node
        else:
            self.insert_node.right = new_node
        
        self.heapify()

    
    def get_node_insertion(self):
        curr = self.root
        
        # get max_lvl
        lvl = 0
        max_lvl = 0
        last_left_node = None
        while curr != None:
            lvl += 1
            if lvl > max_lvl:
                max_lvl = lvl
            last_left_node = curr
            curr = curr.left

        # get all nodes at max_lvl - 1
        lvl = 1
        curr = self.root
        arr = [[curr, 1]]
        last_insert_node = None
        for item in arr:
            lvl += 1
            if item[0].left != None:
                arr.append([item[0].left, lvl])
            if item[0].right != None:
                arr.append([item[0].right, lvl])
        for item in arr:
            if item[1] == max_lvl - 1:
                if item[0].left == None or item[0].right == None:
                    last_insert_node = item[0]
                    break
        
        if last_insert_node == None:
            return last_left_node
        else:
            return last_insert_node

    def extract_min(self):
        pass


    def heapify(self):
        # build heap tree as array
        heap = [self.root]
        for node in heap:
            if node.left != None:
                heap.append(node.left)
            if node.right != None:
                heap.append(node.right)
        
        # heap arr: [4, 50, 7, 55, 90, 87, 2, 89]
        # parent of nth index is : (n/2) - 1 
        # child of n is: 2n + 1, 2n+2
        # root is 0th index
        # last element is (len-1) index
        
        # set curr to last element
        # compare last element to it's parent, if last element is smaller, swap
        # set curr to parent. do this until curr is none

        curr = len(heap) - 1
        while True:
            parent = (curr - 1) // 2
            if parent < 0:
                break
            if heap[curr].data < heap[parent].data:
                heap[curr], heap[parent] = heap[parent], heap[curr]
                curr = parent

    def get_last_node(self):
        stack = []
        curr = self.root
        curr_lvl = 0
        max_lvl = 0
        last_node = None
        last_node_parent = None
        while curr != None or stack != []:
            if curr != None:
                curr_lvl += 1
                stack.append([curr, curr_lvl])                
                if curr_lvl > max_lvl:
                    max_lvl = curr_lvl
                curr = curr.left
            if curr == None:                
                popped = stack.pop()
                curr = popped[0]
                curr_lvl = popped[1]
                if (curr.left == None and curr.right == None and curr_lvl == max_lvl):
                    last_node = curr 
                    if stack != []:                       
                        last_node_parent = stack[-1][0]
                curr = curr.right
                
        return last_node, last_node_parent

    def get_last_node_recurse(self, node, lvl=1, max_lvl=0):
        if node == None:
            return lvl - 1
        else:
            max_lvl = self.get_last_node_recurse(node.left, lvl+1)                            
            self.get_last_node_recurse(node.right, lvl+1)
            if max_lvl  == lvl:
                self.last_node = node
        return self.last_node    

n1 = Node(4)
n1.left = Node(50)
n1.right = Node(7)
n1.left.left = Node(55)
n1.left.right = Node(90)
n1.right.left = Node(87)

mh = MinHeap(n1)
print(mh.get_last_node()[0].data)
print(mh.get_last_node_recurse(n1).data)
mh.insert(2)
print(mh.extract_min())
