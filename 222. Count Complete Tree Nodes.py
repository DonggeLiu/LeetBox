"""
Question:
https://leetcode.com/problems/count-complete-tree-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def exists():
            cur = root
            bits = 1 << (level - 1)

            while (cur and bits > 0):
                if ((bits & mid) == 0):
                    cur = cur.left
                else:
                    cur = cur.right
                bits = bits >> 1
            return cur != None

        if not root:
            return 0
        level = 0

        node = root
        while (node.left):
            level += 1
            node = node.left
        low, high = 1 << level, (1 << (level + 1)) - 1
        while (low < high):
            mid = (low + high) // 2
            if (exists()):
                low = mid
            else:
                high = mid - 1

        return low
