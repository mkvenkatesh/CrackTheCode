# Min Heap (Max Heap)

# Min Heap/Max Heap is a complete (all the levels are filled out and the last
# level is filled from left to right) binary tree (a node has at most 2
# children).

# Min Heap/Max Heap can be easily represented in an array because of the
# completeness property. In an array indexed from 0 to K, 
#   * array[0] -> Root node
#   * array[-1] -> Last node in the heap
#   * array[(n/2)-1] -> Parent node for the node at nth index
#   * array[2n+1], array[2n+2] -> Left and right child node for a node at index n

# Two main operations in a heap structure
# Insert & Extract-Min

class MinHeap:
    def __init__(self, arr):
        self.heap_array = arr

    def insert(self, value):
        # insert the element to the end of the array and perform heapify on that node
        self.heap_array.append(value)
        self.heapify('up')

    def extract_min(self):
        min_val = self.heap_array[0]
        self.heap_array[0], self.heap_array[-1] = self.heap_array[-1], self.heap_array[0]
        self.heap_array.pop()
        self.heapify('down')
        return min_val

    def heapify(self, htype):
        if htype == 'up':
            node_idx = len(self.heap_array) - 1
            while node_idx > 0:
                parent_idx = (node_idx//2)-1
                if self.heap_array[node_idx] < self.heap_array[parent_idx]:
                    self.heap_array[node_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[node_idx]
                node_idx = parent_idx
        elif htype == 'down':
            node_idx = 0
            min_idx = None
            while node_idx < len(self.heap_array):
                left_child = (2 * node_idx) + 1
                right_child = (2 * node_idx) + 2
                if left_child < len(self.heap_array):
                    if self.heap_array[left_child] < self.heap_array[node_idx]:
                        min_idx = left_child
                    if right_child < len(self.heap_array):
                        if min_idx != None and self.heap_array[right_child] < self.heap_array[min_idx]:
                            min_idx = right_child
                        elif self.heap_array[right_child] < self.heap_array[node_idx]:
                            min_idx = right_child
                if min_idx == node_idx:
                    break
                self.heap_array[node_idx], self.heap_array[min_idx] = self.heap_array[min_idx], self.heap_array[node_idx]
                node_idx = min_idx

if __name__ == "__main__":
    heap_arr = [4, 50, 7, 55, 90, 87]
    mh = MinHeap(heap_arr)
    print(heap_arr)
    mh.insert(2)
    print(heap_arr)
    print(mh.extract_min())
    print(heap_arr)
