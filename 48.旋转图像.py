class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:

        n = len(matrix)

        # 第一步，对矩阵进行转置操作
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步，将转置后的矩阵进行左右元素对调
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

        """
        Do not return anything, modify matrix in-place instead.
        """
