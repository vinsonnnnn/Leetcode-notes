from typing import List

#暴力破解
class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    
#哈希表
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            # 先在之前遍历过的数字中查找
            if complement in hashmap:
                return [hashmap[complement], i]

            # 没找到，再存入当前数字
            hashmap[num] = i

        return []