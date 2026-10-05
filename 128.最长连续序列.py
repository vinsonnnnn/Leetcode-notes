class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                for i in range(1, len(num_set)):
                    if current_num + i in num_set:
                        current_streak += 1
                    else:
                        break
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
