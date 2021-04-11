# There are three types of edits that can be performed on strings: insert a
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false

# questions
# can it have whitespace characters?
# is it ascii characters?

# examples
# str1 = baskets
# str2 = basket => true (insert/remove)

# str1 = baskets
# str2 = askets => true (insert/remove)

# str1 = baskets
# str2 = bakets => true (insert/remove)

# str1 = basket
# str2 = brsket => true (replace)

# str1 = kasket
# str2 = basket


# solutions
# check len of strings and see if they are same or off by 1 before proceeding
# Have two pointers, one for each string
# Start both at 0 and match the characters at the pointer indices
# if they match, increase both counts
# if they don't match, increase the counter of bigger string and increment an 'edit_ctr' variable. Proceed to matching characters.
# break away from the loop if edit_ctr is greater than 1 and return false or if we reach the length of the strings
# if string lengths are different, increase edit_ctr by 1 and return true if edit_ctr is 1 else false

class Solution1:
    def validate_input(self, str1, str2):
        if str1 == "" and str2 == "":
            return False

        if abs(len(str1) - len(str2)) <= 1:
            return True
        else:
            return False

    def one_or_less_edit_away(self, str1, str2):
        if (self.validate_input(str1, str2)):
            ptr1 = 0
            ptr2 = 0
            edit_ctr = 0
            while (ptr1 < len(str1)) and (ptr2 < len(str2)):
                if str1[ptr1] == str2[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    edit_ctr += 1
                    if len(str1) > len(str2):
                        ptr1 += 1
                    elif len(str1) < len(str2):
                        ptr2 += 1
                    else:
                        ptr1 += 1
                        ptr2 += 1
                
                if edit_ctr > 1:
                    return False

            if ptr1 != len(str1) or ptr2 != len(str2):
                edit_ctr += 1
            
            if edit_ctr <= 1:
                return True
            else:
                return False


s = Solution1()
print(s.one_or_less_edit_away("pale", "ple"))
print(s.one_or_less_edit_away("pales", "pale"))
print(s.one_or_less_edit_away("pale", "bale"))
print(s.one_or_less_edit_away("pale", "bake"))
print(s.one_or_less_edit_away("baskets", "basket"))
print(s.one_or_less_edit_away("askets", "baskets"))
print(s.one_or_less_edit_away("askets", "dskets"))
print(s.one_or_less_edit_away("askets", "askete"))
