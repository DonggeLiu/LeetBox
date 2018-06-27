"""
Question
https://leetcode.com/problems/increasing-triplet-subsequence/
"""


class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fst = snd = float('inf')
        for num in nums:
            if num > snd:
                return True
            fst = num if fst >= num else fst
            snd = num if snd > num > fst else snd
        return False
