# Given a circular linked list, implement an algorithm that returns the node at
# the beginning of the loop.

# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.

# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

# questions
# 1. singly our doubly?
# 2. do you care about the value in that node?

# solutions
# 1. keep a hash table for each object and if you see that object again, return
#    the hash object
# 2. if node vals can be changed, as you scan the linked list, if the node isn't
#    visited, you can mark off the value as visited and continue. When you see
#    the tail or if you see a visited node again, you know it's the beginning of
#    the loop. Return that next node. 
# 3. recursion - store the node val in temp, mark off as visited, go to next,
#    check if visited, if not store in temp, go all the way until you visit, and
#    then you return the next node back up the layers, while you move temp back
#    to node val

from linked_list import LinkedList

class Solution1:
    def loop_detect(self, ll):
        node = ll.head
        if node == None:
            return None
        hash_table = {}
        while node != None:
            if node not in hash_table:
                hash_table[node] = 1
            else:
                return node
            node = node.next

ll1 = LinkedList(['e', 'd', 'c', 'b' , 'a'])
ll1.head.next.next.next.next.next = ll1.head.next.next
print (ll1.head.next.next)
s = Solution1()
print(s.loop_detect(ll1))

class Solution2:
    def loop_detect(self, ll):
        if ll == None:
            return None        
        elif ll.val == '$$' :
            return ll
        else:
            temp = ll.val
            ll.val = '$$'
            node = self.loop_detect(ll.next)
            ll.val = temp
            return node
s = Solution2()
print(s.loop_detect(ll1.head))