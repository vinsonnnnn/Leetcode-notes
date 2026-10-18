# 路径 + 使用标记
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # 第一步：准备结果、当前路径和使用标记，记录数组长度
        n = len(nums)
        anws = []
        path = []
        used = [False] * n

        def backtrack():

            # 第二步：枚举全部数字，跳过当前排列已经使用的下标
            for i in range(n):
                if used[i]:
                    continue
                # 第三步：选择当前数字，更新使用标记和路径
                used[i] = True
                path.append(nums[i])

                # 第四步：递归填下一位置，返回后撤销本次选择
                backtrack()
                path.pop()
                used[i] = False

            # 第五步：选满全部位置时，复制保存当前排列并结束此分支
            if len(path) == n:
                anws.append(path.copy())
                return
            # 第六步：从空路径开始枚举，搜索结束后返回所有排列

        backtrack()
        return anws
