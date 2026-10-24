# 两次闭区间二分，分别记录边界
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # 左边界第一步：准备闭区间，first=-1表示尚未找到目标
        n = len(nums)
        left, right = 0, n - 1
        first = -1

        # 左边界第二步：区间非空时计算中点并读取元素
        while left <= right:
            mid = left + (right - left) // 2
            value = nums[mid]

            # 左边界第三步：中点太小，排除左半段
            if value < target:
                left = mid + 1

            # 左边界第四步：中点太大，排除右半段
            elif value > target:
                right = mid - 1

            # 左边界第五步：记录当前相等位置，继续寻找更左的目标
            else:
                first = mid
                right = mid - 1

        # 左边界第六步：完全没找到目标，直接返回不存在
        if first == -1:
            return [-1, -1]

        # 右边界第一步：重新初始化搜索区间和右端点记录
        left, right = 0, n - 1
        last = -1
        # 右边界第二步：区间非空时计算中点并读取元素
        while left <= right:
            mid = left + (right - left) // 2
            value = nums[mid]

            # 右边界第三步：中点太小，排除左半段
            if value < target:
                left = mid + 1
            # 右边界第四步：中点太大，排除右半段
            elif value > target:
                right = mid - 1
            else:
                # 右边界第五步：记录当前相等位置，继续寻找更右的目标
                last = mid
                left = mid + 1

        # 右边界第六步：两次边界搜索完成，返回包含两端的位置
        return [first, last]
