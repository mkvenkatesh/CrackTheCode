# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based on
# arrival time) of all animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data
# structures to maintain this system and implement operations such as enqueue,
# dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list
# data structure.

# enqueue
# dequeueAny, dequeueCat, dequeueDog

# solution
# 1. two queueus - one for dog and one for cats. Each node will have animal
#    type, name, sequence. Enqueue will enqueue it into different queues and
#    dequeue any would peek and check which sequence is less and remove that
#    node. If not, dequeue type would remove the node from the appropriate
#    queue.
# 2. just use one array to hold all the animals. pop(0) would pop any animal
#    that's oldest. For cat/dog dequeue, check animal type and pop element at
#    that index. Python will automatically refill the array.
# 3. If you can leverage linked list, you can have one queue for enqueue and
#    dequeue. When it comes to dequeueCat/Dog, start from the front of the queue
#    until you find the animal type, store that in temp var, keep track of prev
#    pointer, make prev.next = curr.next, return temp var

from queue import Queue

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.order = 0
        self.dog_q = Queue()
        self.cat_q = Queue()

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dog_q.enqueue(animal)
        elif isinstance(animal, Cat):
            self.cat_q.enqueue(animal)

    def dequeue_any(self):
        if self.cat_q.peek().order < self.dog_q.peek().order:
            return self.cat_q.dequeue()
        else:
            return self.dog_q.dequeue()  

    def dequeue_cat(self):
        return self.cat_q.dequeue()
    
    def dequeue_dog(self):
        return self.dog_q.dequeue()
    
    def __str__(self):
        print(self.cat_q)
        print(self.dog_q)
        return ""

shelter = AnimalShelter()
shelter.enqueue(Dog("Watson"))
shelter.enqueue(Dog("Pixel"))
shelter.enqueue(Cat("Ella"))
shelter.enqueue(Cat("Boruka"))
shelter.enqueue(Cat("Oscar"))
print(shelter)
print(shelter.dequeue_any().name)
print(shelter.dequeue_cat().name)
