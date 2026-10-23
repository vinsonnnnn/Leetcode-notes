# 闭区间二分，找到就返回


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # 第一步：使用闭区间，初始覆盖所有元素下标
        left, right = 0, len(nums) - 1

        # 第二步：区间仍有元素时，取中点进行比较
        while left <= right:
            mid = left + (right - left) // 2

            # 第三步：找到目标，直接返回元素下标
            if nums[mid] == target:
                return mid

            # 第四步：中点太小，目标或插入位置一定在它后面
            if nums[mid] < target:
                left = mid + 1
            # 第五步：中点太大，继续检查它前面的元素
            if nums[mid] > target:
                right = mid - 1

        # 第六步：搜索结束仍未命中，left就是保持升序的插入位置
        return left
