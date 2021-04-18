# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array). The stack supports the
# following operations: push, pop, peek, and isEmpty.

# example
# Stack: TOP -> 9 -> 3 -> 1
# Temp Stack : TOP -> None

# Stack: TOP -> 3 -> 1
# Temp Stack: TOP -> 9

# Stack: TOP -> 9 -> 1
# Temp Stack: TOP -> 3 (swap)

# Stack: TOP -> 1
# Temp Stack: TOP -> 9 -> 3

# Stack: TOP -> 9
# Temp Stack: TOP -> 1 -> 3 (swap)

# Stack: TOP -> None
# Temp Stack: TOP -> 9 -> 1 -> 3 

# Stack: TOP 1 -> 9
# Temp Stack: TOP -> 3

# Stack: TOP 3 -> 9
# Temp Stack: TOP -> 1 (swap)

# solution
# 1. Pop to the top element from the stack to temp stack. Now peek and compare
#    the top elements of two stacks. If stack.top < temp.top, swap. Proceed with
#    popping elements from stack until stack is empty. Now do the reverse. Pop
#    elements from temp and put it in stack only if stack.top < temp.top swap.
#    Proceed until temp is None. Repeat this until no swap is done when going
#    from stack -> temp -> stack. At the end of stack iteration, you have the
#    largest element in the last so for next time, you can stop before last for
#    popping/comparisons. So number of iterations = size of stack. Each
#    iteration of stack or temp will bring the largest element to the last

# 2. imagine the second stack to be in a sorted order. Initially there's no
#    elements, so  you pop the top of stack1 and insert into stack 2. Now pop
#    next element of stack 1 and see the best fit for this element in stack2. If
#    elements needs to be popped in s2 for the correct placement of popped s1
#    value, pop s2 elements into s2 temporarily, insert s1 popped elem into s2
#    and pop the old values from s2 into s1

from stack import Stack

class StackSort:
    def __init__(self, stack_to_sort):
        self.temp_stack = Stack()
        self.stack_to_sort = stack_to_sort

    def sort_stack(self):
        s = self.stack_to_sort
        t = self.temp_stack
        for i in range(s.size):
            while s.size > i:
                if t.peek() == None:
                    t.push(s.pop())
                else:
                    if (s.peek() < t.peek()):
                        self.swap_tops()
                    else:
                        t.push(s.pop())
            while t.peek() != None:
                s.push(t.pop())

    def swap_tops(self):
        s_top = self.stack_to_sort.pop()
        t_top = self.temp_stack.pop()
        self.stack_to_sort.push(t_top)
        self.temp_stack.push(s_top)

s = Stack()
s.push(7)
s.push(2)
s.push(5)
s.push(1)
s.push(3)
s.push(9)
print(s)
sort = StackSort(s)
sort.sort_stack()
print(s)

class StackSortAnother:
    def __init__(self, stack_to_sort):
        self.sorted_stack = Stack()
        self.stack_to_sort = stack_to_sort

    def sort_stack(self):
        s = self.stack_to_sort
        t = self.sorted_stack
        while s.peek() != None:
            popped = s.pop()
            if t.is_empty():
                t.push(popped)
            else:
                pop_cnt = 0
                while (t.peek() != None and popped > t.peek()):
                    s.push(t.pop())
                    pop_cnt += 1
                t.push(popped)
                for i in range(pop_cnt):
                    t.push(s.pop())
        return t

s = Stack()
s.push(7)
s.push(2)
s.push(5)
s.push(1)
s.push(3)
s.push(9)
print(s)
sort = StackSortAnother(s)
print(sort.sort_stack())