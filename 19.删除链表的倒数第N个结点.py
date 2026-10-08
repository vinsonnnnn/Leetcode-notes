# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # 第一步：让fast先比slow多走n+1步
        for _ in range(n + 1):
            fast = fast.next

        # 第二步：slow和fast一起前进，等到fast到None的时候，slow正好到要删除的节点的前一个节点
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # 第三步：跳过slow.next节点
        slow.next = slow.next.next

        return dummy.next
