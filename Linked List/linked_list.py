# linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, list=[]):
        self.head = None
        if list != []:
            for item in list:
                self.add(item)

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
        print(f"Val {val} added successfully to head of the linked list")

    def pop(self):
        if not self.head:
            print("Nothing to pop. Empty linked list.")
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def remove(self, val):
        ptr = self.head
        prev_ptr = None
        while ptr != None:
            if ptr.val == val:
                print(f"Removing node with val {val}")
                if prev_ptr == None: # Node pointed by head is getting deleted
                    self.head = self.head.next
                else:
                    prev_ptr.next = ptr.next
            prev_ptr = ptr
            ptr = ptr.next

    def __str__(self):
        ptr = self.head
        print_str = []
        while ptr != None:
            print_str.append(str(ptr.val))
            ptr = ptr.next
        return "Linked List: " + " ".join(print_str)

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    print(ll)
    print("Pop value: ", ll.pop())
    ll.add(30)
    print(ll)
    ll.remove(10)
    print(ll)