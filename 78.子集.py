class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 第一步：准备答案、当前路径和数组长度
        ans = []
        path = []
        n = len(nums)

        def backtrack(start):

            # 第二步：每个当前路径都是合法子集，复制保存
            ans.append(path.copy())

            # 第三步：从start开始枚举，让所选下标严格递增
            for i in range(start, n):

                # 第四步：选择当前元素，加入路径
                path.append(nums[i])

                # 第五步：只考虑后续下标，递归结束后撤销本次选择
                backtrack(i + 1)
                path.pop()

        # 第六步：从空路径开始，搜索结束后返回所有子集
        backtrack(0)
        return ans
