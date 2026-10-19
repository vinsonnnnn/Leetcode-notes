# 排序后回溯，用break剪枝


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 第一步：排序得到新列表，准备答案、路径和候选数量
        nums = sorted(candidates)
        ans = []
        path = []
        n = len(nums)

        def backtrack(start, remain):

            # 第二步：剩余目标为0，复制保存完整组合并返回
            if remain == 0:
                ans.append(path.copy())
                return

            # 第三步：从start开始枚举，保证候选下标不递减
            for i in range(start, n):
                value = nums[i]

                # 第四步：数组有序，当前数字太大则后面都不必再试
                if value > remain:
                    break
                # 第五步：选择当前数字，允许重复选择，返回后撤销
                path.append(value)
                backtrack(i, remain - value)
                path.pop()

        # 第六步：从完整目标开始搜索，返回全部组合
        backtrack(0, target)
        return ans
