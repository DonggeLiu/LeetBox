"""
Question
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_stack, ans = [[root]], []
        while level_stack:
            curr_level = level_stack.pop()
            next_level = [child for node in curr_level if node
                          for child in [node.left, node.right] if child]
            ans.append([node.val for node in curr_level if node])
            if next_level:
                level_stack.append(next_level)
        return [level for level in ans if level]
