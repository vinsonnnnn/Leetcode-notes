# 哈希表+递归分治
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        in_positions = {value: i for i, value in enumerate(inorder)}

        def build(pre_start, in_left, in_right):
            if in_left > in_right:
                return None

            root_value = preorder[pre_start]
            root_index = in_positions[root_value]
            left_size = root_index - in_left

            node = TreeNode(root_value)
            node.left = build(pre_start + 1, in_left, root_index - 1)
            node.right = build(pre_start + 1 + left_size, root_index + 1, in_right)

            return node

        return build(0, 0, len(inorder) - 1)
