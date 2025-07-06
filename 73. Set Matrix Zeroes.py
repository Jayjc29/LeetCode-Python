class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zero = []
        column_zero = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero.append(i)
                    column_zero.append(j)                         
        for i in range(m) :
            for j in range(n):
                if i in row_zero or j in column_zero:
                    matrix[i][j] = 0