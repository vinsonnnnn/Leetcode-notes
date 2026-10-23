# 虚拟展开，一次闭区间二分
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        # 第一步：记录行列数，用闭区间覆盖所有虚拟一维下标
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        # 第二步：只要区间非空，就计算待检查的中点
        while left <= right:
            mid = left + (right - left) // 2

            # 第三步：一维下标映射到行列，读取矩阵中间元素
            row, col = mid // cols, mid % cols
            value = matrix[row][col]

            # 第四步：目标存在，立即返回True
            if value == target:
                return True

            # 第五步：依据大小排除已检查的中点和无效半区
            if value > target:
                right = mid - 1
            if value < target:
                left = mid + 1

        # 第六步：区间已空且没有命中，目标不存在
        return False
