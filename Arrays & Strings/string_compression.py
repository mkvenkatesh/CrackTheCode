# Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can assume
# the string has only uppercase and lowercase letters (a - z).

# questions

# solutions
# 1. create a new list and loop through the original string to generate compressed string

class Solution1:
    def compress_string(self, original_str):
        if len(original_str) <= 1:
            return original_str

        compressed_string = [original_str[0]]
        ctr = 1      
        for idx in range(1, len(original_str)):
            if original_str[idx] == original_str[idx-1]:
               ctr += 1
               continue
            else:
                compressed_string.append(str(ctr))
                compressed_string.append(original_str[idx])
                ctr = 1
        
        compressed_string.append(str(ctr))

        if (len(compressed_string)) > len(original_str):
            return original_str
        
        return "".join(compressed_string)

s = Solution1()
print(s.compress_string("aabcccccaaa"))
print(s.compress_string("aabccccca"))
print(s.compress_string("abcdefgh"))
print(s.compress_string("abcdeeffgghhhhhhhhhh"))
            