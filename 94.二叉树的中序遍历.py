# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        # 递归法
        def dfs(node):

            if node is None:
                return node

            dfs(node.left)  # 左：先完整遍历左子树
            ans.append(node.val)  # 中：再记录当前节点值
            dfs(node.right)  # 右：最后遍历右子树

        dfs(root)
        return ans
