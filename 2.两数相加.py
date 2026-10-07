# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:  # carry表示还有进位要处理
            # 第一步：先计算相应的值和进位值
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            total = x + y + carry
            digit = total % 10
            carry = total // 10

            # 第二步：将每个计算好的节点加入到tail之后
            tail.next = ListNode(digit)
            tail = tail.next

            # 第三步：检查l1和l2是否被遍历完
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next
