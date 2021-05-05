# Get, set, clear and update binary numbers

class BitOperations:
    def get_bit(self, bits, i):
        return (bits & (1 << i)) != 0

    def set_bit(self, bits, i):
        return (bits | (1 << i))

    def clear_bit(self, bits, i):
        return (bits & (~(1 << i)))

    def clear_msb_to_ith_bit(self, bits, i):
        mask = (1 << i) - 1
        return bits & mask

    def clear_lsb_to_ith_bit(self, bits, i):
        mask = ~ ((1 << i) - 1)
        return bits & mask
        
    def update_bit(self, bits, i, v):
        mask = ~(1 << i)
        return (bits & mask) | (v << i)

b  = BitOperations()
print(bin(10))
print(b.get_bit(10, 3))
print(b.get_bit(10, 2))

print()
print(bin(10))
print(bin(b.set_bit(10, 2)))

print()
print(bin(10))
print(bin(b.clear_bit(10, 1)))

print()
print(bin(10))
print(bin(b.clear_msb_to_ith_bit(10, 2)))

print()
print(bin(10))
print(bin(b.clear_lsb_to_ith_bit(10, 2)))

print()
print(bin(10))
print(bin(b.update_bit(10, 1, 0)))