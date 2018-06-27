"""
Question
https://leetcode.com/problems/sort-colors/description/
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Compatible with more colours (i.e. numbers) as well
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
