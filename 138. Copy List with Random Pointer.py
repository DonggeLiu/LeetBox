"""
Question:
https://leetcode.com/problems/copy-list-with-random-pointer/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Interweave nodes
        curr = head
        while curr:
            interweave_node = Node(curr.val)
            interweave_node.next = curr.next
            curr.next = interweave_node
            curr = interweave_node.next

        # Map randoms
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        # Extract new linked list
        new_head = head.next
        curr = new_head
        while curr:
            curr.next = curr.next.next if curr.next else None
            curr = curr.next

        return new_head
