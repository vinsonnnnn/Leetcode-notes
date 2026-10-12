# 递归传递上下界


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def valid(node, lower, upper):
            # 空子树没有节点违反要求
            if node is None:
                return True

            # 必须严格位于祖先限定的开区间内
            if not (lower < node.val < upper):
                return False

            return valid(node.left, lower, node.val) and valid(
                node.right, node.val, upper
            )

        return valid(root, float("-inf"), float("inf"))
