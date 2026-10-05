# 一个读指针，一个写指针，当读到非0元素的时候，将元素写入写指针元素中，并将写指针+1

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_pointer = 0
        for read_pointer in range(len(nums)):
            if nums[read_pointer] != 0:
                if read_pointer != write_pointer:
                    nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

        # 将剩余的元素置为0
        for i in range(write_pointer, len(nums)):
            nums[i] = 0
