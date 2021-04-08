# Given two strings, write a method to decide if one is a permutation of the
# other.

# questions
# what about whitespace and case sensitveness?

# examples
# str1 = "abcdefgh"
# str2 = "ghdebcaf" => str1 is a permutation of str2

# str1 = "bbbaaac"
# str2 = "bababac" => str1 is a permutation of str2

# str1 = "abcdef"
# str2 = "moi" => str1 is not a permutation of str2

# Solutions
# if the string lengths are unequal, exit

# 1. Sort both the strings and compare characters (O(nlogn + n))

# 2. build a hash table of str1 with frequency and loop through str2 to match
#    the counts. O(n) but space O(n)

# 2. Optimize
#   build a hash table by looping through both the strings at the same time.
#   when you see a character in str 1 and it doesn't exist in ht, add it and increment counter to 1
#   when you see a character in str 2 and it exists in ht, decrease counter by 1
#   at the end check ht to see if all the counters are 0's

str1 = "abcdefgh"
str2 = "ghdebcaf"

str3 = "abcdef"
str4 = "abcdeg"

class Solution1:
    def check_permutation(self, str1, str2):
        # checks for str1 & 2 to see if lengths match, if they are null etc.
        str1 = sorted(str1)
        str2 = sorted(str2)
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        
        return True

s = Solution1()
print(s.check_permutation(str1, str2))
print(s.check_permutation(str3, str4))
print()

class Solution2:
    def __init__(self):
        self.hash_table = {}

    def check_permutation(self, str1, str2):
        # checks for str1 & 2 to see if lengths match, if they are null etc.
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i] not in self.hash_table:
                    self.hash_table[str1[i]] = 1
                else:
                    self.hash_table[str1[i]] += 1
                
                if str2[i] not in self.hash_table:
                    self.hash_table[str2[i]] = -1
                else:
                    self.hash_table[str2[i]] -= 1

        return self.check_counts_hash_table()

    def check_counts_hash_table(self):
        for v in self.hash_table.values():
            if v != 0:
                return False
        return True

s = Solution2()
print(s.check_permutation(str1, str2))
print(s.check_permutation(str3, str4))
print()        