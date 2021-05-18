# Next Number: Given a positive integer, print the next smallest and the next
# largest number that have the same number of 1 bits in their binary
# representation.

# 3 -> 011
# 4 -> 100
# 5 -> 101
# 6 -> 110

# 7  -> 0111
# 8  -> 1000
# 9  -> 1001
# 10 -> 1010
# 11 -> 1011
# 12 -> 1100
# 13 -> 1101

# Solution
# 1. Given a positive integer, calculate the number of 1s in it. Add 1 to it and
#    then see if the number of 1s match. Keep on incrementing until you hit a
#    binary where number of 1's match with given number. Same for calculating
#    the next smallest number, do a decrement.
# 2. From right to left, the first 01 you see, flip 0 to 1 and then move all the
#    trailing 0's+1 bits between the flipped bit and the 1's. This will get the next
#    biggest number. To get the next smallest number, find the first 10 and flip
#    the 1 to 0 and move all the trailing 1's+1 bit next to the flipped bit

class NextNumber:
    def get_last_bit(self, bits):
        return bits & 1 != 0

    def get_1s(self, val):
        count_1s = 0
        while val > 0:
            if self.get_last_bit(val):
                count_1s += 1
            val = val >> 1
        return count_1s

    def brute_force(self, val):
        val_1s_count = self.get_1s(val)
        next_biggest_number = val + 1
        next_smallest_number = val - 1

        # get next biggest number
        while True:
            if self.get_1s(next_biggest_number) == val_1s_count:
                break
            next_biggest_number += 1
        

        # get next smallest number
        while True:
            if self.get_1s(next_smallest_number) == val_1s_count:
                break
            next_smallest_number -= 1

        print(f"Input: {val}; Binary: {bin(val)}")
        print(f"Next biggest number: {next_biggest_number}; Binary: {bin(next_biggest_number)}")
        print(f"Next smallest number: {next_smallest_number}; Binary: {bin(next_smallest_number)}")


    def optimal_solution(self, val):
        input_num = val
        curr_bit = -1
        prev_bit = -1
        next_biggest_number = 0
        next_smallest_number = 0
        c0 = 0
        c1 = 0
        while input_num > 0:
            curr_bit = self.get_last_bit(input_num)
            if curr_bit == 0:
                c0 += 1
            else:
                c1 += 1

            # next biggest number
            if next_biggest_number == 0 and curr_bit == 0 and prev_bit == 1:
                next_biggest_number = val ^ (1 << (c0 + c1 - 1))
                mask =  ~ ((1 << (c0 + c1 - 1)) - 1)
                next_biggest_number = next_biggest_number & mask
                mask = (1 << (c1 - 1)) - 1
                next_biggest_number |= mask
            # next smallest number
            if next_smallest_number == 0 and curr_bit == 1 and prev_bit == 0:
                next_smallest_number = val ^ (1 << (c0 + c1 - 1))
                mask =  ~ ((1 << (c0 + c1 - 1)) - 1)
                next_smallest_number = next_smallest_number & mask
                mask = ((1 << c1) - 1) << (c0 - 1)
                next_smallest_number |= mask

            if next_biggest_number != 0 and next_smallest_number != 0:
                break

            prev_bit = curr_bit
            input_num = input_num >> 1

        print(f"Input: {val}; Binary: {bin(val)}")
        print(f"Next biggest number: {next_biggest_number}; Binary: {bin(next_biggest_number)}")
        print(f"Next smallest number: {next_smallest_number}; Binary: {bin(next_smallest_number)}")            

n = NextNumber()
print("***** Brute Force Approach *****")
n.brute_force(5)
print()
n.brute_force(11)
print()
n.brute_force(1908)
print()
n.brute_force(13948)
print()

print("\n***** Optimal Approach *****")
n.optimal_solution(5)
print()
n.optimal_solution(11)
print()
n.optimal_solution(1908)
print()
n.optimal_solution(13948)