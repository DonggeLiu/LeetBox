"""
Question:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        Iteration, long but fast
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root, counter = TreeNode(preorder[0]) if preorder else None, 0
        stack = [root]
        for value in preorder[1:]:
            current, parent = TreeNode(value), None
            while stack and stack[-1].val == inorder[counter]:
                parent = stack.pop()
                counter += 1
            if parent:
                parent.right = current
            else:
                stack[-1].left = current
            stack.append(current)
        return root

    def buildTree(self, preorder, inorder):
        """
        Recursion, short but slow
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0]) if preorder else None
        if root:
            index = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
            root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root
