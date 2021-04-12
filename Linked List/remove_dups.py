# Write code to remove duplicates from an unsorted linked list.
#
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# questions
# 1. is it a single linked list or doubly linked list?
# 2. do the linked list have integers or strings or chars?

# examples
# ll = head > 90 -> 10 -> 90 ->20 -> 10 -> 89 -> 20 -> 10 > None

# solutions
# assumption - single linked list
# 1. take the val in the first node, iterate through the list and see if there's another value that matches it and remove it.
#    Move to the next node and repeat the process
# 2. sort the linked list O(n logn) and check adjacent nodes to get rid off duplicates
# 3. take one pass at linked list to build a hash table. using this hash table,
#    delete duplicate nodes in another pass. O(n) time but O(n) space as well

from linked_list import LinkedList

# simple loop and check
class Solution1:
    def remove_duplicates(self, ll):
        ptr1 = ll.head 
        while ptr1 != None:
            ptr2 = ptr1.next
            prev_ptr2 = ptr1
            while ptr2 != None:
                if ptr1.val == ptr2.val:
                    print(f"Value {ptr2.val} is a duplicate. Removing it.")
                    prev_ptr2.next = ptr2.next                    
                else:
                    prev_ptr2 = ptr2
                ptr2 = ptr2.next
            ptr1 = ptr1.next

# use a hash table
class Solution2:
    def build_dict_linkedlist(self, ll):
        hash_table = {}        
        ptr = ll.head
        while ptr != None:
            if ptr.val not in hash_table:
                hash_table[ptr.val] = 1
            else:
                hash_table[ptr.val] += 1
            ptr = ptr.next
        return hash_table

    def remove_duplicates(self, ll):
        # do one pass on linked list to build the ht
        hash_table = self.build_dict_linkedlist(ll)
        # use the hash table to remove duplicates in linked list
        ptr = ll.head.next
        prev_ptr = ll.head
        while ptr != None:
            if hash_table[ptr.val] > 1: # duplicate
                print(f"Value {ptr.val} is a duplicate. Removing it.")
                prev_ptr.next = ptr.next                                
                hash_table[ptr.val] -= 1
            else:
                prev_ptr = ptr
            ptr = ptr.next

ll = LinkedList([10, 20, 89, 10, 20, 90, 10, 90])
print(ll)
s = Solution1()
s.remove_duplicates(ll)
print(ll)

print()

ll = LinkedList([10, 20, 89, 10, 20, 90, 10, 90])
print(ll)
s = Solution2()
s.remove_duplicates(ll)
print(ll)