"""
Question:
https://leetcode.com/problems/maximum-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = collections.deque()
        for num in nums:
            cur_node = TreeNode(num)
            while stack and stack[-1].val < num:
                cur_node.left = stack.pop()
            if stack:
                stack[-1].right = cur_node
            stack.append(cur_node)
        return stack.popleft()
