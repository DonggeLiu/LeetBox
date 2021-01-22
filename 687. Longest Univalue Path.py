"""
Question:
https://leetcode.com/problems/longest-univalue-path/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            left = (1 + left_depth) if (node.left and node.left.val == node.val) else 0
            right = (1 + right_depth) if (node.right and node.right.val == node.val) else 0

            self.ans = max(left + right, self.ans)
            return max(left, right)

        depth(root)

        return self.ans
