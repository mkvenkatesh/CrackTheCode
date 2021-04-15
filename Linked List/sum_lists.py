# You have two numbers represented by a linked list, where each node contains a
# single digit.The digits are stored in reverse order, such that the 1 's digit
# is at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.

# EXAMPLE 
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output:2 -> 1 ->
# 9. That is, 912.

# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. 
# EXAMPLE
# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output:9 -> 1 -> 2.That
# is, 912.

# questions
# can it be decimal or strings?
# can I modify one of the linked list or do I have to return a new object?
# can they be of different lengths?
# single or double

# examples 

# solutions
# 1. two pointers, one for each ll that starts at head
#    take the val at each pointer, add and put the one's digit in a new linked
#    list or use an existing one, store the 10's digit in a var. inc pointers.
#    Add values + remainder and repeat the process. When you have a remainder
#    left at the end, add one more node to the tail to store the value.
# 2. scan both the list to get all the digits, reverse the string, convert to
#    int, add ints, and use the new value to build out a new linked list or
#    modify an existing one by parsing out the 1s, 10s, 100s etc.
# 3/4. for the follow up, we can do #2 (without the reverse), or store object
#    references as you scan the linked lists in an array and reach the tail and
#    perform your addition, use the stored references to be able to go back the
#    list to finish the addition and repoint the head with new node if there's a
#    remainder left

from linked_list import LinkedList

class Solution1:    
    def add_numbers_linked_lists(self, ll1, ll2):
        result_ll = LinkedList()
        l1_ptr = ll1.head
        l2_ptr = ll2.head
        digit_10 = 0
        l1_val = 0
        l2_val = 0
        result_array = []
        while l1_ptr != None or l2_ptr != None or digit_10 != 0:
            if l1_ptr != None:
                l1_val = l1_ptr.val
                l1_ptr = l1_ptr.next
            if l2_ptr != None:
                l2_val = l2_ptr.val    
                l2_ptr = l2_ptr.next

            sum_digits = l1_val + l2_val + digit_10
            digit_10 = sum_digits // 10
            digit_1 = sum_digits % 10
            result_array.append(digit_1)
            l1_val = 0
            l2_val = 0

        for i in range(len(result_array)-1, -1, -1):
            result_ll.add(result_array[i])

        return result_ll

ll1 = LinkedList([8, 7, 9])
ll2 = LinkedList([5, 8, 6])
print(ll1)
print(ll2)
s = Solution1()
print(s.add_numbers_linked_lists(ll1, ll2))
        
# use recursion
class Solution2:
    result_ll = LinkedList()
    def add_numbers_linked_lists(self, ll1, ll2, carry=0):
        if (ll1 == None) and (ll2 == None) and carry == 0:
            return
        else:        
            if ll1 == None:
                ll1_val = 0
                ll1_next = None
            else:
                ll1_val = ll1.val
                ll1_next = ll1.next

            if ll2 == None:
                ll2_val = 0
                ll2_next = None
            else:
                ll2_val = ll2.val
                ll2_next = ll2.next

            digit_sum = ll1_val + ll2_val + carry
            carry = digit_sum // 10
            digit_sum %= 10            
            self.add_numbers_linked_lists(ll1_next, ll2_next, carry)
            self.result_ll.add(digit_sum)


ll1 = LinkedList([8, 7, 9])
ll2 = LinkedList([6])
print(ll1)
print(ll2)
s = Solution2()
s.add_numbers_linked_lists(ll1.head, ll2.head)
print(s.result_ll)