from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 空链表或者是单节点已经有序
        if head is None or head.next is None:
            return head

        # 第一步：快慢指针，找到左半段的尾节点
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 第二步：保存右半段的入口节点
        right_head = slow.next
        slow.next = None

        # 第三步：对左右半段分别进行排序（递归）
        left = self.sortList(head)
        right = self.sortList(right_head)

        # 第四步：迭代合并两条左右有序链表
        dummy = ListNode(0)
        tail = dummy
        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left is not None else right

        return dummy.next
