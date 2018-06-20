"""
Question:
https://leetcode.com/problems/subsets/description/
"""


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [c for l in range(len(nums)+1) for c in itertools.combinations(nums, l)]
