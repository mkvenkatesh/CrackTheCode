# Queue (FIFO)

# add(item)
# remove()
# peek()
# is_empty()

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.back = None
    
    def add(self, item):
        print(f"Adding {item} to the back of the queue")
        new_node = Node(item)
        new_node.next = self.back
        self.back = new_node

    def remove(self):
        back = self.back
        prev = self.back

        if not back:
            return None
        elif back.next == None:
            self.back = None
            return back.data
        else:
            while back.next != None:
                prev = back
                back = back.next
                
            prev.next = None
            return back.data        

    def peek(self):
        back = self.back
        if not back:
            return None
        else:
            while back.next != None:
                back = back.next
            return back.data
    
    def is_empty(self):
        return self.back == None

    def __str__(self):
        print_str = ["Queue: "]
        back = self.back
        while back != None:
            print_str.append(str(back.data))
            if back.next != None:
                print_str.append(", ")
            back = back.next
        return "".join(print_str)

if __name__ == "__main__":
    q = Queue()
    print("Queue is empty? ", q.is_empty())
    q.add(10)
    print("Peek Queue: ", q.peek())
    print("Queue is empty? ", q.is_empty())
    print(q)
    print("Remove queue item: ", q.remove())
    print(q)
    q.add(10)
    q.add(20)
    q.add(30)
    q.add(40)
    print(q)
    print("Remove Queue: ", q.remove())
    print("Remove Queue: ", q.remove())
    print("Peek Queue: ", q.peek())
    print("Remove Queue: ", q.remove())
    print("Remove Queue: ", q.remove())
    print("Remove Queue: ", q.remove())
    print(q)