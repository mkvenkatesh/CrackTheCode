# Pairwise Swap: Write a program to swap odd and even bits in an integer with as
# few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit
# 3 are swapped, and so on).

# Hints:#145,#248,#328,#355

# 1011
# 10110 (<<1)
#  0101 (>>1)
#  0111

# 1010 >> 1 =  0101
# 1 << 1    =    10
#           =  0111

# even bits shift left and odd bits shift right
# get even bits - go through the num bit by bit - 01 and shift left by 1 - 0 1 0
# get odd bits - 11 - shift right by 1 - 0 1 1
# 010
#  011

# Solution
# 1. Get the last two bits, swap and build a string. Continue doing this for
#    rest of the bits
# 2. Get last two bits and if they are the same, continue to get the new two
#    bits. If they are different, xor the original number by 3 left shifted by 2
#    * (pairs encountered - 1).
# 3. Shift even bits left and odd bits right and OR both the numbers to get the
#    desired output. To get only the odd bits, & original number with 101010..
#    (0xAAAA..). To get only the even bits, & original number wth 1010..(0xAAA..)
#    right shifted by 1

class PairWiseSwap:
    def get_last_bit(self, bits):
        return bits & 1 != 0

    def pair_swap(self, num):
        bit1 = None
        bit2 = None
        num_cpy = num
        pair_cnt = 0
        while num_cpy > 0:
            if self.get_last_bit(num_cpy):
                bit1 = 1
            else:
                bit1 = 0

            num_cpy >>= 1

            if self.get_last_bit(num_cpy):
                bit2 = 1
            else:
                bit2 = 0

            num_cpy >>= 1

            if bit1 != bit2:
                num = num ^ (3 << (2 * pair_cnt))            
            
            pair_cnt += 1

        return num

    def pair_swap_optimal(self, num):
        # get odd bits
        odd = num & 0xAAAAAAAA
        # get even bits
        even = num & (0xAAAAAAAA >> 1)

        # shift odd bits right once & even bits left once and OR them to get the final number
        odd = odd >> 1
        even = even << 1

        return odd | even

p = PairWiseSwap()
num = 11
print(bin(num))
print(bin(p.pair_swap(num)))
num = 12
print(bin(num))
print(bin(p.pair_swap(num)))

print()

num = 11
print(bin(num))
print(bin(p.pair_swap_optimal(num)))
num = 12
print(bin(num))
print(bin(p.pair_swap_optimal(num)))