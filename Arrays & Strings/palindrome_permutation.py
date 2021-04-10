# Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome does
# not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

# questions
# how to treat white space characters in the string?
# is it case sensitive or insensitive

# Examples
# input: "hi3ih32gjg2"
# output: True

# solutions
# 1. find all permutations of input string and then for each permutation check
#    if the string and reverse of that string matches, if so print true and exit - O(n!)

# 2. sort the string (o(n*log n)) and check if adjacent characters are equal.
#    When they are not equal for the first time, increment break_ctr to 1 and
#    move one. The second time you encounter a difference in adjacent char,
#    break away and print false. O(nlogn) + O(n)

# 3. build a dict of the frequency of chars. Loop through the dict and if you
#    find only one odd number, return True - O(n) but o(n) space

# 4. Create a bit vector and set 1 to each char bit when you first see it. See
#    the same one again, flip to 0. If the bit vector is 0 or has one one, the
#    string is a palindrome

str = "Tact Coa"

class Solution1:
    def validate_input(self, str):
        pass

    def has_palindrome_perm(self, str):
        self.validate_input(str)
        str = sorted(str.lower())
        break_ctr = -1
        i = 0
        while i < len(str) - 1:
            if str[i] == ' ':
                i += 1
                continue
            
            if str[i] != str[i+1]:
                break_ctr += 1
                i += 1
            else:
                i += 2

            if (break_ctr > 0) or (break_ctr == 0 and i == len(str)-1):
                return False
        return True

s = Solution1()
print(s.has_palindrome_perm(str))


class Solution2:
    def validate_input(self, str):
        pass

    def has_palindrome_perm(self, str):
        self.validate_input(str)
        hash_table = {}
        for char in str.lower():
            if char == ' ':
                continue
            if char not in hash_table:
                hash_table[char] = 1
            else:
                hash_table[char] += 1
        
        odd_cnt = 0
        for val in hash_table.values():
            if val % 2 == 1:
                odd_cnt += 1
            if odd_cnt > 1:
                return False
        
        return True

s = Solution2()
print(s.has_palindrome_perm(str))
 
class Solution3:
    def validate_input(self, str):
        pass

    def has_palindrome_perm(self, str):
        bit_vector = 0
        for char in str.lower():
            if char == ' ':
                continue
            
            ord_char = ord(char)
            bit_vector ^= 1 << ord_char
        
        if (bit_vector & (bit_vector - 1)) == 0:
            return True
        else:
            return False

s = Solution3()
print(s.has_palindrome_perm(str))
 
        
