# 辨认有序半区，一次二分
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 第一步：初始化闭区间，覆盖所有可能的目标位置
        left, right = 0, len(nums) - 1

        # 第二步：区间非空时计算当前中点
        while left <= right:
            mid = left + (right - left) // 2

            # 第三步：中点命中，返回旋转后数组中的实际下标
            if nums[mid] == target:
                return mid

            # 第四步：左半区有序，判断目标是否位于左侧值域
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 第五步：右半区有序，判断目标是否位于右侧值域
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # 第六步：所有位置均已排除，目标不存在
        return -1
