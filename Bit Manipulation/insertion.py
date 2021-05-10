# Insertion - You are given two 32-bit numbers, N and M, and two bit positions,
# i and j. Write a method to insert M into N such that M starts at bit j and
# ends at bit i. You can assume that the bits j through i have enough space to
# fit all of M. That is, if M = 10011, you can assume that there are at least 5
# bits between j and i. You would not, for example, have j = 3 and i = 2,
# because M could not fully fit between bit 3 and bit 2.

# EXAMPLE
# Input: N   10000000000, M 10011, i 2, j 6 
# Output:N = 10001001100

# Solution
# 1. Make i to j bits 0 in N. Shift M left to i bits to pad the right side with 0'set. Bitwise OR N and M

class BitSplice:
    def __init__(self):
        pass

    def clear_bit(self, bit, i):
        mask = ~(1 << i)
        return bit & mask

    def insert(self, N, M, i, j):
        for k in range(i, j+1):
            N = self.clear_bit(N, k)
        M = M << i
        N = N | M
        return N

    def better_insert(self, N, M, i, j):
        # j = 3
        # 010000
        # 001111
        # 110000
        mask1 = ~((1 << (j + 1)) - 1)

        # i = 1
        # 000010
        # 000001
        mask2 = (1 << i) - 1

        # 110000
        # 000001 |
        # 110001
        clear_i_j = mask1 | mask2
        return (N & clear_i_j) | (M << i)



N = 19876
M = 89
i = 2
j = len(bin(M)) - 2 + i
b = BitSplice()
print(bin(N))
print(bin(M))
print(bin(b.insert(N, M, i, j)))
print(bin(b.better_insert(N, M, i, j)))