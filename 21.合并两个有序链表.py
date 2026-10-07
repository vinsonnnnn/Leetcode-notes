# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:

        # 定义一个虚假的头部dummy，他的next是真的头部
        dummy = ListNode(0)
        tail = dummy

        # 按顺序把两个list接入到tail之后
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # 如果有一个list插入完之后，将另一个没插完的list全部插入
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
