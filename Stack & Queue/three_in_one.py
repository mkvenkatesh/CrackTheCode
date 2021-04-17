# Describe how you could use a single array to implement three stacks.

# push top of the array, pop top of the array, peek top of the array, is_empty() - O(1)

# solutions
# 1. use array of arrays
# 2. if you have a fixed size array, divide by 3 and use modulo to define the
#    lower and upper limits of each stack. use three top pointers to represent
#    where the top of each stack would be
# 3. above is fixed but you can also make it variable by shifting the elements
#    when more space is needed for a stack and making the array circular

class Stack:
    STACK_SIZE = 3
    NUM_STACKS = 3
    stack_array = []
    stack_ctr = 0

    def __init__(self):
        if Stack.stack_ctr < self.NUM_STACKS:
            self.stack_start = Stack.stack_ctr * self.STACK_SIZE
            self.stack_end = self.stack_start + self.STACK_SIZE
            self.top = self.stack_start            
            Stack.stack_ctr += 1
        else:
            raise OverflowError("No more stacks can be created")

    def push(self, item):
        if self.top >= self.stack_end:
            raise OverflowError("No more space in stack. Pop some elements before pushing them")
        else:
            Stack.stack_array.append(item)
            self.top += 1
    
    def pop(self):
        if self.top <= self.stack_start:
            raise OverflowError("Stack is empty. No elements to pop")
        else:
            self.top -= 1
            return Stack.stack_array[self.top]

    def peek(self):
        if self.top < self.stack_start:
            raise OverflowError("Stack is empty. No elements to peek")
        else:
            return Stack.stack_array[self.top]

    def is_empty(self):
        return self.top == self.stack_start

    def __str__(self):
        print_str = ["Stack: "]
        for i in range(self.stack_start, self.top):
            print_str.append(str(Stack.stack_array[i]))
            if i < self.top - 1:
                print_str.append(", ")
        if len(print_str) == 1:
            return "Stack is empty"
        else:
            return "".join(print_str)

s1 = Stack()
s2 = Stack()
s3 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
print(s1)
print("Pop element: ", s1.pop())
print("Pop element: ", s1.pop())
print("Pop element: ", s1.pop())
print(s1)


s2.push(10)
s2.push(20)
s2.push(30)
print(s2)
print("Pop element: ", s2.pop())
print("Pop element: ", s2.pop())
print("Pop element: ", s2.pop())
print(s2)


s3.push(10)
s3.push(20)
s3.push(30)
print(s3)
print("Pop element: ", s3.pop())
print("Pop element: ", s3.pop())
print("Pop element: ", s3.pop())
print(s3)