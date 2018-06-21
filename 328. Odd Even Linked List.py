"""
Question
https://leetcode.com/problems/odd-even-linked-list/description/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        odd_head = odd_pointer = head
        even_head = even_pointer = head.next

        while odd_pointer:
            odd_pointer.next = even_pointer.next if even_pointer.next else even_head
            odd_pointer = odd_pointer.next if even_pointer.next else None

            even_pointer.next = odd_pointer.next if odd_pointer else None
            even_pointer = even_pointer.next if even_pointer.next else even_pointer

        return odd_head
