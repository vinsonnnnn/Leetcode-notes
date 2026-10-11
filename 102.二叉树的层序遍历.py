# 队列BFS广度优先搜索
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            # 第一步：计算本层节点数
            level_size = len(queue)
            level = []

            # 第二步：把本层的节点加入队列
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # 第三步：将下一层（左右孩子）添加到队列中，用于下一次计算
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            # 第四步：本层计算完之后，将本层结果加入result
            result.append(level)

        return result
