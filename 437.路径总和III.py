# 前缀和 + 哈希表 + 递归DFS

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 第一步：定义一个哈希表前缀和
        prefix_count = {0: 1}

        # 递归DFS
        def dfs(node, current_sum):
            if node is None:
                return 0
            current_sum += node.val
            # 第二步：在前缀和中查询目标前缀和,统计以当前节点为终点的合法路径
            paths = prefix_count.get(current_sum - targetSum, 0)

            # 第三步：将当前的总和加入到前缀和哈希表当中
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            # 第四步：对左右孩子进行DFS递归
            paths += dfs(node.left, current_sum)
            paths += dfs(node.right, current_sum)

            # 第五步：离开当前分支：只撤销本节点贡献的这一次
            prefix_count[current_sum] -= 1
            if prefix_count[current_sum] == 0:
                del prefix_count[current_sum]

            return paths

        return dfs(root, 0)
