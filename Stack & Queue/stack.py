# Stack (LIFO)

# push(item)
# pop()
# peek()
# is_empty()

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, item):
        # print(f"Pushing {item} into top of stack")
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if not self.top:
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            self.size -= 1
            return popped
    
    def peek(self):
        if not self.top:
            return None
        else:
            return self.top.data
    
    def is_empty(self):
        if not self.top:
            return True
        else:
            return False

    def __str__(self):
        top = self.top
        print_str = ['Stack: [']
        while top != None:
            print_str.append(str(top.data))
            if top.next != None:
                print_str.append(", ")
            top = top.next
        return "".join(print_str) + ']'

if __name__ == "__main__":
    s = Stack()
    print("Stack is empty? ", s.is_empty())
    s.push(10)
    print("Peek Stack: ", s.peek())
    print("Stack is empty? ", s.is_empty())
    print(s)
    print("Pop stack: ", s.pop())
    print(s)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    print(s)
    print("Pop stack: ", s.pop())
    print("Pop stack: ", s.pop())
    print("Peek stack: ", s.peek())
    print("Pop stack: ", s.pop())
    print("Pop stack: ", s.pop())
    print("Pop stack: ", s.pop())
    print (s)