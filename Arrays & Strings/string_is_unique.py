# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# q: what characters is used? ascii (128), ascii-extended (256), utf-8?

# Example
# str = "abcdefgh " -> unique
# str = "abcdb efgha " -> non-unique

str1 = "abcdefgh "
str2 = "abcdb efgha "

# take the first character, compare against every other character to see if it
# exist. repeat this for all characters - (n-1) + (n-2) ...1 = O(n^2). Break
# away if there's a match
class Solution1:
    def is_unique(self, str):
        for i in range(len(str)-1):
            for j in range(i+1, len(str)-1):
                if str[i] == str[j]:
                    return f'{str} is not unique!'
        return f'{str} is unique!'

s = Solution1()
print(s.is_unique(str1))
print(s.is_unique(str2))

# sort the string (O(n logn)) and loop through the string to see if adjacent
# characters are different and break way if they are same
class Solution2:
    def is_unique(self, str):
        str1 = sorted(str)
        for i in range(len(str)-1):
            if str1[i] == str1[i+1]:
                return f'{str} is not unique!'
        return f'{str} is unique!'

s = Solution2()
print(s.is_unique(str1))
print(s.is_unique(str2))

# loop through the string, build hash table. if a key already exists, the string
# is not unique = O(n) but space is O(n) as well
class Solution3:
    def is_unique(self, str):
        hash_table = {}
        for char in str:
            if char in hash_table:
                return f'{str} is not unique!'
            hash_table[char] = None
        return f'{str} is unique!'

s = Solution3()
print(s.is_unique(str1))
print(s.is_unique(str2))

# use a bit vector
class Solution4:
    def is_unique(self, str):
        bit_vector = 0
        for i in str:
            char_ord = ord(i)
            if (bit_vector & (1 << char_ord)) != 0:
                return f'{str} is not unique!'
            bit_vector = bit_vector | (1 << char_ord)
        print(bin(bit_vector), '\n', bit_vector)
        return f'{str} is unique!'

s = Solution4()
print(s.is_unique(str1))
print(s.is_unique(str2))        