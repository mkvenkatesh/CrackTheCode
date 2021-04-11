# Write an algorithm such that if an element in an MxN matrix is 0, its entire
# row and column are set to 0.

# questions

# examples

# 1 2 3 4 5 4
# 6 7 0 9 1 5
# 8 0 1 8 9 3
# 7 3 9 2 1 4
#     |
#     V
# 1 0 0 4 5 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 7 0 0 2 1 4

# solutions
# 1. loop through mxn matrix with two loops and when a 0 is found in a cell,
#    have a loop set 0 for all the rows in that column followed by another loop
#    that sets 0 for all the columns in that row. - O(mn * (m+n))

# 2. Same as before but note down the indices where value is 0 using a row and
#    column list. loop i,j through mxn and if i in row list, set all column
#    values to 0 for that row. if i is not in row, see if j is and set it to 0

# 3. Same as before but use the first row and first column to store the
#    information about which rows/cols to make it 0. Just note down 0
#    applicability for first row or col separately and nullify at the end if
#    necessary. If not, the whole array would become 0 as row nullification
#    would make the column nullification all 0

class Solution1:
    def zero_matrix(self, matrix):

        # note down 0 applicability for first row and column separately
        first_row_has_0s = False
        first_col_has_0s = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_has_0s = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_0s = True
                break

        # use the first row/col to store the 0 applicability for rest of the
        # array (1 to len on row/col)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # nullify all rows/cols based on first row/col 0 info
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        # nullify 1st row/col if the original information stored about 0
        # applicability on the first row or col is true
        for i in range(len(matrix)):
            if first_col_has_0s:
                matrix[i][0] = 0
        for i in range(len(matrix[0])):
            if first_row_has_0s:
                matrix[0][i] = 0

matrix = [
     [0,2,3,4,5,4],
     [6,7,0,9,1,5],
     [8,0,1,8,9,3],
     [7,3,9,2,1,4]
]

s = Solution1()
s.zero_matrix(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
           