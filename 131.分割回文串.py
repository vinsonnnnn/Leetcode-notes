# 回溯 + 直接检查回文


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # 第一步：准备字符串长度、全部答案和当前分割方案
        path = []
        n = len(s)
        ans = []

        def backtrack(start):
            # 第二步：整个字符串都已分割，复制保存完整方案并返回
            if start == n:
                ans.append(path.copy())
                return

            # 第三步：枚举当前段的结束下标，截取连续非空子串
            for end in range(start, n):
                piece = s[start : end + 1]

                # 第四步：当前段不是回文，跳过该切点
                if piece != piece[::-1]:
                    continue

                # 第五步：选择当前段，递归后面的字符，返回后撤销
                path.append(piece)
                backtrack(end + 1)
                path.pop()

        # 第六步：从字符串开头搜索，结束后返回全部分割方案
        backtrack(0)
        return ans
