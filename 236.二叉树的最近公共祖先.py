# 递归DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):

            # 第一步：处理终止情况；空节点返回None，遇到p或q返回该节点
            if node is None or node is p or node is q:
                return node

            # 第二步：分别搜索左右子树，接收目标节点或已经找到的祖先
            left = dfs(node.left)
            right = dfs(node.right)

            # 第三步：两侧都有结果，说明目标分居两侧，当前节点就是LCA
            if left is not None and right is not None:
                return node

            # 第四步：只有一侧有结果就向上传递；两侧都为空则返回None
            return left if left is not None else right

        # 从根开始执行上述四步，返回最终的原节点引用
        return dfs(root)
