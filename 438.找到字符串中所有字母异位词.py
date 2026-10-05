from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_need = {}
        s_window = {}
        result = []

        right = 0
        if len(s) < len(p):
            return result
        for char in p:
            p_need[char] = p_need.get(char, 0) + 1

        for right, char in enumerate(s):
            s_window[char] = s_window.get(char, 0) + 1
            if right >= len(p):
                left_char = s[right - len(p)]
                s_window[left_char] -= 1
                if s_window[left_char] == 0:
                    del s_window[left_char]

            if s_window == p_need and right >= len(p) - 1:
                result.append(right - len(p) + 1)
        return result
