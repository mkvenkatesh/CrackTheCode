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
        self.front = None
    
    def add(self, item):
        print(f"Adding {item} to the back of the queue")
        new_node = Node(item)
        if self.back:
            self.back.next = new_node
        self.back = new_node
        if not self.front:
            self.front = self.back     

    def remove(self):
        if not self.front:
            return None
        else:
            temp = self.front.data
            self.front = self.front.next
            return temp       

    def peek(self):
        if not self.front:
            return None
        else:
            return self.front.data
    
    def is_empty(self):
        return self.back == None

    def __str__(self):
        print_str = ["Queue: "]
        front = self.front
        while front != None:
            print_str.append(str(front.data))
            if front.next != None:
                print_str.append(", ")
            front = front.next
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