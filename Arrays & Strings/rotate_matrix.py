# Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
# place?

# questions
# 

# examples
#  1 2 3        7 4 1
#  4 5 6    =>  8 5 2
#  7 8 9        9 6 3
# 
# (0,0) -> (0,2) -> (2,2) -> (2,0) -> (0,0)

# (0,1) -> (1,2) -> (2,1) -> (1,0) -> (0,1)

# (1,1) -> (1,1)

# Solutions
# 1. outer loop i goes from 0 to n//2
#    inner loop j goes from 0 to n-1
#       m(i,j), m(j, n-i-1) = m(j, n-i-1), m(i,j)



class Solution1:
    def rotate_matrix_90(self, matrix):
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix) - i - 1):
                new_i = i
                new_j = j
                temp = matrix[new_i][new_j]

                for k in range(4):                                     
                    new_i, new_j = new_j, len(matrix) - new_i - 1 
                    matrix[new_i][new_j], temp = temp, matrix[new_i][new_j]

matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]   

s = Solution1()
s.rotate_matrix_90(matrix)


for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()


print()
matrix = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42],
            [43, 44, 45, 46, 47, 48, 49]
        ]   

s = Solution1()
s.rotate_matrix_90(matrix)


for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()
