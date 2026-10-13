# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if root is None:
            return

        stack = [root]

        while stack:
            node = stack.pop()

            # 修改连接前，先保存原孩子；右先压，左后压
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

            # 栈顶是先序下一个节点；最后一个节点的right为None
            node.right = stack[-1] if stack else None
            node.left = None

        """
        Do not return anything, modify root in-place instead.
        """
