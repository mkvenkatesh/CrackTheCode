# Draw Line: A monochrome screen is stored as a single array of bytes, allowing
# eight consecutive pixels to be stored in one byte. The screen has width w,
# where w is divisible by 8 (that is, no byte will be split across rows). The
# height of the screen, of course, can be derived from the length of the array
# and the width. Implement a function that draws a horizontal line from (x1, y)
# to (x2, y).

# The method signature should look something like:
# drawline(byte[] screen, int width, int x1, int x2, int y)

# Hints: #366, #381, #384, #391

# Screen width = 2 bytes = 16 bits (divisible by 8); length = 4 bytes; height = length/width = 2
# screen [] = [
# [00000000], [00000000]
# [00000000], [00000000]
# ]

# e.g:
# x1=1, y=0
# x2=3, y=0

# 00000000
# 01110000 (|)
# ---------
# 01110000

# 1 = 2^1 - 1
# 11 = 3 = 2^2 - 1
# 111 = 7 = 2^3 - 1

# (2^n -1) << (8-x2-1)

# length = 4
# width = 16 bits/8 = 2 bytes
# length/width = 4/2 = 2 rows (height)
# y = 0 or 1
# x1 <= x2 and x2 <= (row*8)-1
# get all the row bytes

# for each byte, if x2 > (8*(arry_index+1))-1, then build a string with 1's
# ((8*(arry_index+1))-1)-x1-+1 and left shift it appropriately and or the byte. 

# if x2 <= (8*(arry_index+1))-1, then build a string of 1's, left shift it and
# or the byte with the mask

import math

class DrawLine:
    def drawline(self, screen, width, x1, x2, y):        
        height = (len(screen) * 8) // width

        if (width % 8 != 0) or (x1 > x2) or (y > (height - 1)) or (x1 < 0) or (x2 > (width - 1)):
            raise ValueError("Error: Out of bounds")
        
        # x1 = 0, x2 = 2 (0-2)
        # x1 = 5, x2 = 10 (5-7) (8-10)
        # x1 = 8, x2 = 10 (8-10)
        # x1 = 0, x2 = 16 (0-7) (8-15) (16)

        # Calculate which array to modify given x1 and x2. Use y
        # Lower bound = (y * width) [0, 16]
        # Upper bound = ((y + 1) * width) [16, 32]
        screen_array_start_index = (y * width) // 8
        screen_array_stop_index = ((y + 1) * width) // 8
        row_index = -1
        for i in range(screen_array_start_index, screen_array_stop_index):
            row_index += 1
            if x1 >= (row_index + 1) * 8:
                continue

            if x2 < (row_index + 1) * 8:
                # x1 & x2 are in the same byte
                # do ops to flip bits to 1 for x1-x2 in ith array
                shift = 8 - (x1 % 8) - (x2 % 8) - 1
                mask = int(math.pow(2, x2 - x1 + 1) - 1) << shift
                screen[i] = bin(screen[i] | mask)
                break
            else:
                # do ops to flip bits to 1 for x1 to end of ith array
                mask = int(math.pow(2, (((row_index + 1) * 8) - 1) - x1 + 1) - 1)
                screen[i] = bin(screen[i] | mask)
                x1 = (row_index + 1) * 8
            
dl = DrawLine()
screen = [0,0,0,0]
width = 16
dl.drawline(screen, width, 0, 5, 0)
dl.drawline(screen, width, 4, 15, 1)
print(screen)