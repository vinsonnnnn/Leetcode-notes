class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        right = 0
        len_max = 0
        for right, char in enumerate(s):
            if char in last_index:
                left = max(left, last_index[char] + 1)

            last_index[char] = right
            len_max = max(len_max, right - left + 1)
        return len_max
