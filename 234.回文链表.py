from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        node = head

        # 第一次遍历链表，将链表的值放入栈中
        while node is not None:
            stack.append(node.val)
            node = node.next

        # 第二次遍历链表，从栈的尾部取值，跟链表的值逐一对比
        node = head
        while node is not None:
            if node.val != stack.pop():
                return False
            node = node.next

        return True
