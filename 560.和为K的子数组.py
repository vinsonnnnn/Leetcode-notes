# 前缀和
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # 用一个字典进行计数，记录每种和的出现次数
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count.get(prefix_sum - k, 0)
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
        return count
