# 迭代中序DFS
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while current is not None or stack:
            # 先深入左子树，保存沿途待访问的节点
            while current is not None:
                stack.append(current)
                current = current.left

            # 左子树已处理，正式访问当前节点
            node = stack.pop()
            count += 1

            if count == k:
                return node.val
            # 接下来处理右子树，仍按中序规则继续
            current = node.right

        # 题目保证1 <= k <= n，合法输入不会走到这里
        raise ValueError("k must be between 1 and the number of nodes")
