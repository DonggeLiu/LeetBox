"""
Question:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        def search(is_left):
            lo, hi = 0, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                mid_num = nums[mid]
                if (is_left and (mid_num == target)) or (mid_num > target):
                    if (mid_num == target) and ((mid - 1 < 0) or (nums[mid - 1] != target)):
                        return mid
                    hi = mid - 1
                else:
                    if (mid_num == target) and ((mid + 1 >= n) or nums[mid + 1] != target):
                        return mid
                    lo = mid + 1
            return -1

        return [search(True), search(False)]
