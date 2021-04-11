# Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation
# of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation
# of"erbottlewat").

# question
# 1. s1 & s2 are different lengths and can have spaces?

# examples
# s1 = erbottlewat 
# s2 = waterbottle => s2 is rotation of s1
#
# s1 = erbottlewate
# s2 = waterbottles => s2 is not a rotation of s1
#
# s1 = erbottl e1'wat
# s2 = 1'waterbottl e => s2 is rotation of s1
#
# s1 = wata
# s2 = atwa => s2 is not a rotation of s1

# s1 = wata
# s2 = ataw => s2 is a rotation of s1


# if strings are different length, quit

# solutions
# 1. concatenate str1 to itself and see if s2 is substring of s1.

class Solution1:
    def string_rotation(self, str1, str2):
        str1 += str1
        if str2 in str1: # one substring call
            return True
        else:
            return False

str1 = "erbottlewat"
str2 = "waterbottle"
s = Solution1()
print(s.string_rotation(str1, str2))