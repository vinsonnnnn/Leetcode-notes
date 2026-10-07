from typing import Optional


# Definition for singly-linked list.
# LeetCode 已提供 ListNode，提交时保持以下定义为注释。
# 本地需要构造节点时，可使用这段节点类定义。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        fast = head
        slow = head

        # 第一步：快慢指针首先确定是否有环，寻找相遇节点
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # 第二步：找到相遇节点之后，寻找环的入口
            if fast is slow:
                finder = head

                while finder is not slow:
                    finder = finder.next
                    slow = slow.next

                return finder

        return None
