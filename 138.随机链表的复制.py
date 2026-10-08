"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copies = {None: None}

        # 第一步：只创建新节点，建立一一对应的映射
        cur = head
        while cur is not None:
            copies[cur] = Node(cur.val)
            cur = cur.next

        # 第二步：连接副本节点的 next 和 random
        cur = head
        while cur is not None:
            new_node = copies[cur]
            new_node.next = copies[cur.next]
            new_node.random = copies[cur.random]
            cur = cur.next

        return copies[head]
