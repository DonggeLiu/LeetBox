"""
Question:
https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        head = l3
        while l1 or l2:
            if l1:
                l3.val += l1.val
                l1 = l1.next
            if l2:
                l3.val += l2.val
                l2 = l2.next
            if l3.val > 9:
                l3.val -= 10
                l3.next = ListNode(1)
                l3 = l3.next
            elif l1 or l2:
                l3.next = ListNode(0)
                l3 = l3.next
        return head
