"""
Question:
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        siblings = [root] if root else ans

        while siblings:
            ans.append(max([sibling.val for sibling in siblings]))
            siblings = [child for parent in siblings
                        for child in [parent.left, parent.right] if child]

        return ans
