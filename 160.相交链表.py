from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        seen = set()
        node = headA

        # 将A链表中的节点加入到seen当中
        while node is not None:
            seen.add(node)
            node = node.next

        # 检验B链表中的节点是否在seen中
        node = headB
        while node is not None:
            if node in seen:
                return node

            node = node.next

        return None
