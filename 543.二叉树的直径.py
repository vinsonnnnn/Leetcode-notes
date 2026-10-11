# 递归DFS解法

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        # 定义计算深度的递归函数
        def depth(node):
            nonlocal diameter

            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 经过当前节点的最长路径
            diameter = max(diameter, left_depth + right_depth)

            # 返回的是子树深度，节点本身+最长的一边
            return 1 + max(left_depth, right_depth)

        depth(root)

        return diameter
