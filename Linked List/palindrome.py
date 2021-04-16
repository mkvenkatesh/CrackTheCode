# Implement a function to check if a linked list is a palindrome.

# questions
# 1. singly or doubly


# examples
# a->b->b->a
# a->b->b->a->b

# solution
# 1. scan through the linkedlist and store the chars in an array. scan through
#    the linked list again and check if node val matches the array vals from the
#    end. O(n) time and space
# 2. reverse the linked list and check the first half or regular linked list
#    with the reversed linked list. For reversing you can simply iterate through
#    the list and build a new list. Everytime you do this the list is reversed
#    because the elements are inserted near the head
# 3. you can use two pointers. one pointer iterates through the list. another
#    pointer iterates 2x fast. When the first pointer reaches the middle, second
#    would be at end. So push all the elements in the first half of the list
#    into a stack and when the first pointer reaches the midde, pop the stack
#    and compare the elements to the rest of the node elements.
# 4. use recursion. base case is that the middle element is a palindrome so now
#    check for equality of element before and after the middle and go all the
#    way to the 1st and last element
from linked_list import LinkedList

# use an array for storing and comparing
class Solution1:
    def check_palindrome(self, ll):
        temp = []
        node = ll.head
        length = 0
        while node != None:
            temp.append(node.val)
            node = node.next
            length += 1
        
        node = ll .head
        idx = -1
        i = 0
        while i <= (length//2):
            if node.val != temp[idx]:
                return False
            node = node.next
            idx -= 1
            i += 1
        
        return True

ll = LinkedList(['a', 'a', 'b', 'c', 'b', 'a', 'a'])
s = Solution1()
print(s.check_palindrome(ll))

# revese a list and compare values
class Solution2:
    def reverse_linkedlist(self, ll):
        node = ll.head
        rev_ll = LinkedList()
        ll_length = 0        
        while node != None:
            rev_ll.add(node.val)
            node = node.next
            ll_length += 1
        return rev_ll, ll_length

    def is_equal(self, ll, rev, length):
        head = ll.head
        tail = rev.head
        i = 0
        while head != None and tail!= None and i <= length//2:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
            i += 1
        return True

    def check_palindrome(self, ll):
        reversed, length = self.reverse_linkedlist(ll)
        return self.is_equal(ll, reversed, length)

ll = LinkedList(['a', 'a', 'b', 'c', 'b', 'a', 'a'])
s = Solution2()
print(s.check_palindrome(ll))

# use two pointers. One 1x fast and another 2x fast. when 2x fast reaches end,
# 1x would be in middle. Use stack to  push all node values from head to middle
# and then as you scan the rest of the list, compare the node val with popped
# stack values.
class Solution3:
    def check_palindrome(self, ll):
        first_half_stack = []
        one_x = ll.head
        two_x = ll.head
        while two_x != None and two_x.next != None:
            first_half_stack.append(one_x.val)
            one_x = one_x.next
            two_x = two_x.next.next
        
        # if the linked list has odd elements, skp the middle element
        if (two_x != None):
            one_x = one_x.next
        
        # Finish scanning the linked list with one_x and match with popped stack elements
        while one_x != None:
            if one_x.val != first_half_stack.pop():
                return False
            one_x = one_x.next
        
        return True

ll = LinkedList(['a', 'a', 'b', 'b', 'a', 'a'])
s = Solution3()
print(s.check_palindrome(ll))

# recursion
class Solution4:
    def check_palindrome(self, ll):
        ll_length = self.get_length(ll)
        return self.is_palindrome(ll.head, ll_length)[1]
    
    def get_length(self, ll):
        length = 0
        node = ll.head
        while node != None:
            length += 1
            node = node.next
        return length
    
    def is_palindrome(self, front, length):
        if (length == 0 or length == 1):
            if length == 0:
                back = front
            else:
                back = front.next
            return back, True
        else:
            back, result = self.is_palindrome(front.next, length - 2)
            if result:
                if back.val == front.val:
                    back = back.next
                    return back, True
                else:
                    return back, False
            else:
                return back, False

ll = LinkedList(['a', 'a', 'b', 'b', 'a', 'a'])
s = Solution4()
print(s.check_palindrome(ll))