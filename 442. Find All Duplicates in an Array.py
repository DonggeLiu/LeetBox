"""
Question:
(https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set()
        return [num for num in nums if (num in nums_set) or nums_set.add(num)]
