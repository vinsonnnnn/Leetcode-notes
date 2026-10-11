# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        # 先判断第一对子节点是否为镜像，构造辅助函数mirror
        def mirror(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            # 利用递归判断第一对子节点内部两侧是否为镜像

            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)
