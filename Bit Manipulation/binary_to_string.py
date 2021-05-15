# Binary to String - Given a real number between O and 1 (e.g., 0.72) that is
# passed in as a double, print the binary representation. If the number cannot
# be represented accurately in binary with at most 32 characters, print "ERROR:'

# 0.893 = 8 * 10^-1 + 9 * 10^-2 + 3 * 10^-3
# 0.893 * 10 = 8 * 10^0 + 9 * 10^-1 + 3 * 10^-2 = 8.93 
# 0.10011 * 2 = 1 * 2^0 + 0 * 2^-1 + 0 * 2^-2 + 1*2^-3 + 1* 2^-4 = 1.0011
# 0.10011 * 2 = 1.0011
# 0.893 * 2 = 1.786 * 2 = 1.572 * 2 = 1.144 * 2 = 0.288 * 2...
#             -           -           -           -


class BinaryToString:    
    def convert_to_str(self, decimal_num):
        if decimal_num <= 0 or decimal_num >= 1:
            return "Error"
        bin_str = ['.']
        while decimal_num > 0:
            r = decimal_num * 2
            if r >= 1:
                bin_str.append('1')
                decimal_num = r - 1
            else:
                bin_str.append('0')
                decimal_num = r
            if len(bin_str) > 32:
                return "Error"
        return "".join(bin_str)
        
b = BinaryToString()
print(b.convert_to_str(0.7))
