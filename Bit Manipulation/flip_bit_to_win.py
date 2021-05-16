# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0
# to a 1. Write code to find the length of the longest sequence of 1s you could
# create.

# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8

# 10011011

class FlipBitToWin:
    def get_bit(self, bits, i):
        mask = 1 << i
        return bits & mask != 0

    def set_bit(self, bits, i):
        mask = 1 << i
        return bits | mask

    # if 0 flip the bit and note it down 11011101100
    def longest_sequence_1s(self, num):
        init_seq_count = 0
        flip_seq_count = -1
        flip_bits = False
        max_seq = 0
        while num > 0:
            if self.get_bit(num, 0):
                init_seq_count += 1
                if flip_bits:
                    flip_seq_count += 1
            else:
                if not flip_bits:
                    flip_bits = True
                    init_seq_count += 1
                    flip_seq_count += 1
                else:
                    init_seq_count = flip_seq_count + 1
                    flip_seq_count = 0
            num = num >> 1
            if init_seq_count > max_seq:
                max_seq = init_seq_count

        return max_seq

f = FlipBitToWin()
print(f.get_bit(20, 2))
print(f.set_bit(20, 0))
print()
print(bin(1908))
print(f.longest_sequence_1s(1908))
print()
print(bin(1775))
print(f.longest_sequence_1s(1775))
