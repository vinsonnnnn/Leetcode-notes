# 回溯，只构造合法前缀


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # 第一步：准备答案和当前括号路径
        ans = []
        path = []

        def backtrack(left, right):
            # 第二步：长度达到2n，在合法前缀约束下就是完整答案
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            # 第三步：左括号未用满，选择左括号，递归后撤销
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()

            # 第四步：有未匹配的左括号，选择右括号，递归后撤销
            if left > right:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        # 第五步：从尚未放置任何括号的状态开始搜索
        backtrack(0, 0)
        # 第六步：搜索结束，返回全部有效字符串
        return ans
