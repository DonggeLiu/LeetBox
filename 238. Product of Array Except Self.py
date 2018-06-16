"""
Question:
https://leetcode.com/problems/product-of-array-except-self/description/
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def compute_products(refs, ans):
            product = 1
            for i, ref in enumerate(refs):
                ans[i] = ans[i] * product
                product *= ref
            return ans[::-1]

        return compute_products(nums[::-1], compute_products(nums, [1]*len(nums)))
