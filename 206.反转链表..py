# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head

        while cur is not None:
            next_node = cur.next  # 先把原链表的下一个节点保存下来
            cur.next = prev  # 用反转后的链表的头节点替换原链表的下一个节点
            prev = cur  # 更新 prev，让它指向已反转链表的新头节点
            cur = next_node  # 恢复原本的cur.next

        return prev
