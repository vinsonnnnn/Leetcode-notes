from typing import List


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        rows = len(matrix)
        cols = len(matrix[0])
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        result = []

        # 外层嵌套一个大循环，当遍历到左边超过右边，上边超过下边，遍历结束
        while left <= right and top <= bottom:

            # 从左到右遍历上边界
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # 上边界下移
            top += 1
            if top > bottom:
                break

            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            # 右边界左移
            right -= 1
            if left > right:
                break

            # 从右到左遍历下边界
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            # 下边界上移
            bottom -= 1
            if top > bottom:
                break

            # 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            # 左边界右移
            left += 1
            if left > right:
                break

        return result
