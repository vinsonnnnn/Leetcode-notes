# 回溯


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 第一步：兼容空输入，避免把空字符串当作一个答案
        if not digits:
            return []

        # 第二步：建立数字字符到字母的映射，准备答案和路径
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        path = []
        n = len(digits)

        def backtrack(index):
            # 第三步：每个数字都已选择字母，拼接保存并结束此分支
            if index == n:
                ans.append("".join(path))
                return

            # 第四步：获取当前数字对应的候选字母，逐一尝试
            digit = digits[index]
            for letter in phone[digit]:
                # 第五步：选择、递归下一位置、撤销本次选择
                path.append(letter)
                backtrack(index + 1)
                path.pop()

        # 第六步：从第一个数字开始搜索，返回全部组合
        backtrack(0)
        return ans
