"""
Question
https://leetcode.com/problems/find-the-duplicate-number/description/
"""


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common(1)[0][0]
