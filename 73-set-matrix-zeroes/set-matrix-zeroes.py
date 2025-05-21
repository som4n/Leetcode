class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        row_arr= [False]*m
        col_arr= [False]*n

        for row in range(m):
            for col in range(n):
                if matrix[row][col]== 0:
                    row_arr[row] = True
                    col_arr[col] = True

        for row in range(m):
            for col in range(n):
                if row_arr[row] or col_arr[col]:
                    matrix[row][col] = 0