# Implement an algorithm to delete a node in the middle (i.e., any node but the
# first and last node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.

# EXAMPLE
# Input:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f


# questions
# 1. does the node that you are given access to, can it be the first node?
# 2. are you given the length of the linked list?

# examples
# a | a->b : no deletion.
# a->b->c: only b can b deleted
# a->b->c->d: b or c can be deleted

# solution Assumption: you are not given the first node
# 1. given a node, check if node.next is none and return else, get node.next.val
#    and store it in node.val inc ptr to next node and repeat the same. store
#    reference to previous pointer as well when node.next is done, go back to
#    prev pointer and set prev.next to none

from linked_list import LinkedList

class Solution1:
    def delete_middle_node(self, node):
        if node == None or node.next == None:
            return
        else:
            node.val = node.next.val
            node.next = node.next.next
            return

ll = LinkedList([5, 4, 3, 2, 1])
s = Solution1()
print(ll)
s.delete_middle_node(ll.head.next.next.next.next)
print(ll)

