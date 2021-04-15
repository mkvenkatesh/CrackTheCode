# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x. If x is
# contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right
# partitions.

# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5] 
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# questions
# 1. positive integers?

# examples
# Input: 1 -> 10 -> 5 -> 8 -> 2 [Partition=5]
# Output: 1 -> 2 -> 10 -> 5 -> 8

# solutions
# 1. Two pointers. both pointers move together checking to see if the node value
#    is bigger than or equal to x. If it is, anchor one of the pointer at this
#    point. Move the other pointer forward. Now if any node value is less than
#    x, swap the node at current pointer with anchor. Increment
#    current pointer and repeat process. O(n)
# 2. Have two linked lists O(n) space. Scan the linked list O(n) and anything less
#    than x put in ll 1, else ll 2. Now build a new linked list by merging
#    ll1 and ll2. O(n)

from linked_list import LinkedList

class Solution1:
    def partition_list(self, ll, x):
        if ll == None:
            return
        
        runner = ll.head
        anchor = ll.head
        while runner != None:
            if runner.val < anchor.val:
                runner.val, anchor.val = anchor.val, runner.val

            if runner.val < x:                
                anchor = anchor.next
            runner = runner.next


ll1 = LinkedList([3, 5, 8, 5, 10, 2, 1])
ll2 = LinkedList([1, 10, 5, 8, 2])
s = Solution1()
s.partition_list(ll1, 5)
s.partition_list(ll2, 5)
print(ll1)
print(ll2)