# 递归分治法


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            # 中间值创建根节点；这里创建的是节点，不是数组
            node = TreeNode(nums[mid])

            # 每次递归返回对应子树的根节点，连接到当前节点
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(nums) - 1)
