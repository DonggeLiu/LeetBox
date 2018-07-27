"""
Question:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def connect(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        while root and root.left:
            curr = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next.left if root.next else None
                root = root.next
            root = curr
