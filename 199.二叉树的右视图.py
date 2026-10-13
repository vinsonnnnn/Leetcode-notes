# 队列BFS ：把每层元素从左到右加入队列，最后取出的元素就是本层最右侧的元素
from typing import Optional
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:

            # 当前层有多少个节点，先固定下来
            level_size = len(queue)
            for i in range(level_size):
                # 从前往后从队列中取出节点
                node = queue.popleft()

                # 从前往后从队列中取出节点
                if i == level_size - 1:
                    result.append(node.val)

                # 孩子加入下一层，保持从左到右的次序
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return result
