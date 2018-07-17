"""
Question:
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes, ans, step = collections.deque([root, None]), [[]], -1
        while nodes[0]:
            node = nodes.popleft()
            ans[-1].append(node.val)
            nodes.extend([child for child in [node.left, node.right] if child])
            if not nodes[0]:
                step = 0 - step
                nodes.append(nodes.popleft())
                ans.extend([ans.pop()[::step], []])
        return ans[:-1]
