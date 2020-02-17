"""
Question:
https://leetcode.com/problems/maximum-product-subarray/
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        imax = imin = r = nums[0]

        for num in nums[1:]:
            # If num is negative, it will swap the max with the min
            if num < 0:
                imax, imin = imin, imax

            # Accumulate product if product turns out to be larger/smaller
            imax = max(num * imax, num)
            imin = min(num * imin, num)

            # Compare with the global max
            r = max(imax, r)
        return r
