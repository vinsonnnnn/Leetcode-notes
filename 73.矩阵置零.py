from typing import List


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        # 利用两个布尔变量来记录第一行和第一列原本是否有0元素（因为后续要先改变第一行第一列的0元素来当作标记）
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # 第一个循环，如果内部有0元素，则将第一行和第一列相应位置置0，作为标记
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 第二个循环，根据第一行第一列作为标记，将相应内部其他位置置0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 最后根据一开始记录的布尔变量，来决定是否将第一行和第一列置0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
