"""
Question:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        looker, ptr = head, None

        for i in range(n):
            looker = looker.next
        while looker:
            looker, ptr = looker.next, ptr.next if ptr else head
        if ptr:
            ptr.next = ptr.next.next

        return head if ptr else head.next
