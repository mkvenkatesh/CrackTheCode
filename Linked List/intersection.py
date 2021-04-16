# Given two (singly) linked lists, determine if the two lists intersect. Return
# the inter­secting node. Note that the intersection is defined based on
# reference, not value.That is, if the kth node of the first linked list is the
# exact same node (by reference) as the jth node of the second linked list, then
# they are intersecting.

# questions
# 1. is the length of two lists known?
# 2. what is there are more than one node that are intersecting?

# examples

# l1: 1 (0x10) -> 2 (0x11) -> 3 (0x12) -> 4 (0x13)
# l2: 1 (0x14) -> 2 (0x15) -> 3 (0x12) => l2 intersects l1 at 0x12 reference

# l1: 1 (0x10) -> 2 (0x11) -> 3 (0x12) -> 4 (0x13)
# l2: 1 (0x14) -> 2 (0x15) -> 3 (0x16) -> 4 (0x17) => l2 doesn't intersect l1

# solutions
# 1. scan both the list with two pointers. check the next reference for both the
#    pointers. If they don't match, go to next. If they have same reference,
#    return the next node. Repeat until one of the list becomes null or if a
#    match is found.

from linked_list import LinkedList

class Solution1:
    def check_intersection(self, ll1, ll2):
        ll1 = ll1.head
        ll2 = ll2.head
        if ll1 == None or ll2 == None:
            return False
        while ll1 != None and ll2 != None:
            if ll1 == ll2:
                return ll1         
            ll1 = ll1.next
            ll2 = ll2.next
        return False

ll1 = LinkedList([1, 2, 3])
ll2 = LinkedList()
ll2.head = ll1.head
s = Solution1()
print(s.check_intersection(ll1, ll2))