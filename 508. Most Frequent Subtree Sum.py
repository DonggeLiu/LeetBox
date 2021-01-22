"""
Question:
https://leetcode.com/problems/most-frequent-subtree-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.sums = defaultdict(int)

        def computeTreeSum(node: TreeNode) -> int:
            if not node:
                return 0
            left = computeTreeSum(node.left)
            right = computeTreeSum(node.right)
            tree_sum = left + right + node.val
            self.sums[tree_sum] += 1
            return tree_sum

        if not root:
            return []
        computeTreeSum(root)
        max_sum = max(self.sums.values())
        return [k for k in self.sums.keys() if self.sums[k] == max_sum]
