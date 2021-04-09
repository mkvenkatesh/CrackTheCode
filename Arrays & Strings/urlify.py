# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional
# characters,and that you are given the "true" length of the string. 

# EXAMPLE
# Input:  "Mr John Smith    ", 13 
# Output: "Mr%20John%20Smith"

# questions
# the string always ends with a non-space character?
# what about tabs or other white-space characters?

# examples
# input: " m joj ns      "
# output:"%20m%20joj%20ns"

# Solutions
# 1. loop through the original string and copy characters to another array. when
#    you encounter space, replace with %20. join the array as a string at the
#    end. - O(n) but O(n) space

# 2. loop i from max_len to 0, at true length, swap that char with i. reduce
#    true length and i. check if the char at true length is a space and if so
#    add 02% to chr[i] to i-2. reduce i by 3 and true length by 3. O(n)

class Solution1:
    def urlify(self, str, true_len):
        str = list(str)
        right_ptr = len(str) - 1
        left_ptr = true_len - 1
        while left_ptr > 0:
            if str[left_ptr] == ' ':
                str[right_ptr] = '0'
                str[right_ptr-1] = '2'
                str[right_ptr-2] = '%'
                right_ptr -= 2
            else:
                str[right_ptr], str[left_ptr] = str[left_ptr], str[right_ptr]
            right_ptr -= 1
            left_ptr -= 1
        print("".join(str))

str = "Mr John Smith    "
s = Solution1()
s.urlify(str, 13)