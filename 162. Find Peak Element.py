"""
Question:
https://leetcode.com/problems/find-peak-element/
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (j + i) // 2
            if nums[m] > nums[m + 1]:
                j = m
                continue
            i = m + 1
        return i
