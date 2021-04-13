# Implement an algorithm to find the kth to last element of a singly linked
# list.

# questions
# what to do if k is past head?
# is tail pointed?

# examples
# find 4th to last
# ll = head > 1 > 2 > 3 > 4 > 5 > 6 > None => 3

# solutions
# 1. put it in an array and get the index value of len-k O(n) with space O(n)
# 2. one pass to get the length. we know need to stop at length-k, so take one
#    more pass and stop there and get the element - O(n)

from linked_list import LinkedList

# use array
class Solution1:
    def kth_to_last(self, ll, k):
        temp_array = []
        ptr = ll.head
        
        while ptr != None:
            temp_array.append(ptr.val)
            ptr = ptr.next
        
        if k >= len(temp_array):
            return None
        return temp_array[-k]

# do two passes. One pass gets length. Another pass to stop at k-to-last and get
# the val
class Solution2:
    def kth_to_last(self, ll, k):
        ptr = ll.head
        ll_length = 0
        while ptr != None:
            ll_length += 1
            ptr = ptr.next
        
        ptr = ll.head
        k_to_last = ll_length - k
        seen_ctr = 0
        while ptr != None:
            if seen_ctr == k_to_last:
                return ptr.val
            ptr = ptr.next
            seen_ctr += 1


# use recursion
class Solution3:
    kth_val = None
    def kth_to_last(self, ptr, k, length=0):
        if ptr == None:
            return length-k
        else:
            kth_idx_val = self.kth_to_last(ptr.next, k, length+1)
            if self.kth_val == None:
                if length == kth_idx_val:
                    self.kth_val = ptr.val
                    kth_idx_val = self.kth_val
                return kth_idx_val
            else:
                return self.kth_val


class Solution4:
    def kth_to_last(self, node, k, root=True):
        if not node:
            return 0, 0
        else:
            depth, val = self.kth_to_last(node.next, k, False)
            depth += 1
            if depth == k:
                if root:
                    return node.val
                else:
                    return depth, node.val
            
            if root:
                return val
            else:            
                return depth, val


ll = LinkedList([1, 2, 3, 4, 5, 6, 7])
print(ll)

s = Solution1()
print(s.kth_to_last(ll, 3))

s = Solution2()
print(s.kth_to_last(ll, 3))

s = Solution3()
print(s.kth_to_last(ll.head, 7))

s = Solution4()
print(s.kth_to_last(ll.head, 4))