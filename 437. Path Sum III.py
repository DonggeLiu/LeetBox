"""
Question:
https://leetcode.com/problems/path-sum-iii/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:

        def sumPath(node):
            if not node:
                return []
            self.ans += (node.val == sum)
            path = [node.val]
            for v in sumPath(node.left):
                self.ans += (v + node.val) == sum
                path.append(v + node.val)
            for v in sumPath(node.right):
                self.ans += (v + node.val) == sum
                path.append(v + node.val)
            return path

        sumPath(root)
        return self.ans
