"""
Question:
https://leetcode.com/problems/permutations/description/
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [pre_pmt+[num]
                for num in nums for pre_pmt in self.permute([x for x in nums if num != x])
               ] if len(nums) else [[]]