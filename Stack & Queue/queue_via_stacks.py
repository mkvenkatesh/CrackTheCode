# Queue via Stacks - Implement a MyQueue class which implements a queue using
# two stacks.

# example
# s1
# push 1, 2, 3
# s1 -> 3 -> 2 -> 1
# pop() should get 1 since it was first inserted
# pop all elements from s1 and push to s2
# s2 -> 1 -> 2 -> 3
# pop s2 element (queue pop)
# s2 -> 2 -> 3
# if a new element needs to be inserted, it should go to back of the queue
# s1 -> 5 -> 4
# 

# Solution
# 1. Have two stacks. When an item needs to be inserted into the queue, insert
#    into stack1. If an item needs to be popped, pop from s2 if it's not empty,
#    if not move all items from stack1 to stack2 (except the last one, which you
#    can return for the pop). New pushes will go to s1. Pops will empty s2 as
#    long as there's something there. If its not there, initiate move operation
#    from s1 to s2 except last item.

from stack import Stack

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def add(self, item):
        self.s1.push(item)

    def remove(self):
        if not self.s2.top:
            self.move_stacks(self.s1, self.s2)
        return self.s2.pop()

    def move_stacks(self, s1, s2):
        while s1.top != None:
            s2.push(s1.pop())

    def peek(self):
        if not self.s2.top != None:
            self.move_stacks(self.s1, self.s2)
        return self.s2.top

    def is_empty(self):
        return self.s1.top == None and self.s2.top == None
    
    def __str__(self):
        return self.s1.__str__() + "\n" + self.s2.__str__()

q = MyQueue()
print(q.is_empty())
print(q)
q.add(1)
q.add(2)
q.add(3)
print(q)
print(q.remove())
print(q)
q.add(4)
q.add(5)
print(q)
print(q.remove())
print(q.remove())
print(q)
print(q.remove())
print(q)
print(q.remove())
print(q)