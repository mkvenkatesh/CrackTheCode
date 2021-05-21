# Conversion - Write a function to determine the number of bits you would need
# to flip to convert integer A to integer B.

# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

# Solutions

# 1. Get last bit from each integer and compare them. If they are different,
#    increment counter. Right shift both numbers and proceed with the rest of
#    the comparison. O(n)

# 2. you can xor the 2 numbers can count the number of 1's in it

class Conversion:
    def get_last_bit(self, num):
        return num & 1 != 0
    
    def flip_count(self, a, b):
        f_cnt = 0
        while a > 0 or b > 0:
            if self.get_last_bit(a) != self.get_last_bit(b):
                f_cnt += 1
            a = a >> 1
            b = b >> 1
        
        return f_cnt

    def flip_count_optimized(self, a, b):
        flip_cnt = 0
        c = a ^ b
        while c > 0:
            if self.get_last_bit(c):
                flip_cnt += 1
            c >>= 1
        return flip_cnt

c = Conversion()
a = 290
b = 150
print(bin(a))
print(bin(b))
print(c.flip_count(a, b))
print(c.flip_count_optimized(a, b))
