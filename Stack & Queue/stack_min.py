# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in 0(1) time.

# questions
# linked list or array implementation for the stack?

# examples
# stack: 10 9 8 1 1 7 2
# min: 1 (suppose 1 is popped, next min is 8)

# solutions
# 1. calculate min in the 'push' method and maintain min values in a stack or
#    array and top element will give the min. 'remove' method takes off top from
#    both the original stack and the min stack/array - O(1) but O(n) space to
#    store min stack/array. Once you have a min, you can ignore insertion of
#    elements into min stack if stack value > min. We pop min stack when remove
#    is called for stackval <= min
# 2. You can maintain one variable for min that calculates min in the push
#    method. In remove, as long as value you are removing is greater than min,
#    min is still valid. If it's <= min, min needs to be recalculated.

from stack import Stack, Node

class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.min = Stack()
    
    def push(self, item):
        super().push(item)
        if (self.min.is_empty() or self.min.peek() >= item):
            self.min.push(item)
    
    def pop(self):
        popped = super().pop()
        if (popped and popped <= self.min.peek()):
            self.min.pop()
        return popped
    
    def min_stack(self):
        if not self.min.is_empty():
            return self.min.peek()
        else:
            return None

s = StackMin()
print(s)
s.push(10)
s.push(9)
print(s)
print("Min: ", s.min_stack())
s.push(8)
s.push(1)
print(s)
print("Min: ", s.min_stack())
s.push(1)
s.push(7)
s.push(2)
print(s)
print("Min: ", s.min_stack())
s.pop()
s.pop()
print(s)
print("Min: ", s.min_stack())
s.pop()
print(s)
print("Min: ", s.min_stack())
s.pop()
print(s)
print("Min: ", s.min_stack())
s.pop()
print(s)
print("Min: ", s.min_stack())
s.pop()
print(s)
print("Min: ", s.min_stack())
s.pop()
print(s)
print("Min: ", s.min_stack())