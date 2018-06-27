"""
Question:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
The fastest solution 
"""


class Solution:
    def __init__(self):
        self.k = 0
        self.result = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root.left and self.k < k:
            self.kthSmallest(root.left, k)

        self.k += 1
        if self.k == k:
            self.result = root.val

        if root.right and self.k < k:
            self.kthSmallest(root.right, k)
        return self.result


"""
A shorter but slower solution
"""


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def add_subtree(node):
            return add_subtree(node.left) + [node] + add_subtree(node.right) if node else [None]
        return [node.val for node in add_subtree(root) if node][k-1]
