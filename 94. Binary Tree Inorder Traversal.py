"""
Question:
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        Recursion
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal(root.left) + [root.val] \
                + self.inorderTraversal(root.right) if root else []
            
    
    def inorderTraversal(self, root):
        """
        Iteration, as the question requested
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = [root] if root else []
        ans = []
        while nodes:
            node = nodes.pop()
            
            while node.left and (node.left not in ans):
                nodes.append(node)
                node = node.left
            
            ans.append(node)
            if node.right:
                nodes.append(node.right)
                
        return [node.val for node in ans]
            
            
        
        