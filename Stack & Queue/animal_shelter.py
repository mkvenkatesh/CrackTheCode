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

class AnimalShelter(Queue):
    def dequeue_any(self):
        if not self.is_empty():
            return super().dequeue()
        else:
            return None
    
    def dequeue_animal_type(self, type):
        if not self.is_empty():
            if self.peek()[0] == type:
                return self.dequeue_any()
            elif self.front.next != None:
                curr = self.front
                prev = None
                while curr.data[0] != type:
                    prev = curr
                    curr = curr.next
                temp = curr.data
                prev.next = curr.next
                return temp
            else:
                return None
        else:
            return None

    def dequeue_cat(self):
        return self.dequeue_animal_type('cat')
    
    def dequeue_dog(self):
        return self.dequeue_animal_type('dog')
    
shelter = AnimalShelter()
shelter.enqueue(('cat', 'ella'))
shelter.enqueue(('cat', 'boruka'))
shelter.enqueue(('cat', 'oscar'))
shelter.enqueue(('dog', 'pixel'))
shelter.enqueue(('dog', 'watson'))
shelter.enqueue(('dog', 'india'))
print(shelter)
print("Dequeue Dog: ", shelter.dequeue_dog())
print("Dequeue Dog: ", shelter.dequeue_dog())
print("Dequeue Any: ", shelter.dequeue_any())
print("Dequeue Cat: ", shelter.dequeue_cat())
print("Dequeue Dog: ", shelter.dequeue_dog())
print("Dequeue Dog: ", shelter.dequeue_dog())
print("Dequeue Any: ", shelter.dequeue_any())
print("Dequeue Any: ", shelter.dequeue_any())
print(shelter)