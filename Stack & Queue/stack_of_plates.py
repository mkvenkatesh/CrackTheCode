# Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the
# previous stack exceeds some threshold. Implement a data structure SetOfStacks
# that mimics this. SetOfStacks should be composed of several stacks and should
# create a new stack once the previous one exceeds capacity. SetOfStacks.push()
# and SetOfStacks.pop() should behave identically to a single stack (that is,
# pop() should return the same values as it would if there were just a single
# stack).

# FOLLOW UP 
# Implement a function popAt(int index) which performs a pop operation on a
# specific sub-stack.

# question

# examples
# setofstacks = [stack1, stack2, stack3 etc]

# solution
# 1. keep an array for setofstacks. As each stack fills up, create a new stack
#    and store the reference to the next index in the array.  Push operation
#    will insert the item in the current stack if it has space, if not a new
#    stack is created and item is pushed into it. For pop, if the current stack
#    is exhausted, remove that reference from array and pop the element from the
#    previous stack. Each array can either hold sub-stacks as arrays or
#    linkedlists


from stack import Stack

class SetOfStacks:
    STACK_SIZE = 3
    def __init__(self):
        self.set_of_stacks = []
    
    def push(self, item):
        if (self.set_of_stacks == [] or self.set_of_stacks[-1][1] == SetOfStacks.STACK_SIZE):
            s = Stack()
            self.set_of_stacks.append([s, 1])
            s.push(item)
        else:
            self.set_of_stacks[-1][0].push(item)
            self.set_of_stacks[-1][1] += 1

    def pop(self, index=None):
        if (self.set_of_stacks == []):
            return None
        else:
            if index == None:
                index = -1
            popped = self.set_of_stacks[index][0].pop()
            self.set_of_stacks[index][1] -= 1
            if self.set_of_stacks[index][1] == 0:
                self.set_of_stacks.pop(index)
            return popped

    def __str__(self):
        print_str = ["Stack:"]
        for i in range(len(self.set_of_stacks)):
            print_str.append("\n\t")
            print_str.append(self.set_of_stacks[i][0].__str__())
        return "".join(print_str)


s = SetOfStacks()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.pop(0))
print(s.pop(0))
print(s.pop(0))
print(s.pop())
print(s)