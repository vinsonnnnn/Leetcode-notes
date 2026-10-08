# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next is not None and prev.next.next is not None:
            # 第一步：先确定本来的顺序
            first = prev.next
            second = first.next
            after = second.next

            # 第二步：进行顺序交换
            first.next = after
            second.next = first
            prev.next = second

            prev = first

        return dummy.next
