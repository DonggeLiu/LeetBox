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
        return self.compute_products(znums[::-1], self.compute_products(nums, [1]*len(nums)))
        
    def compute_products(self, nums, ans):
        product = 1
        for i, num in enumerate(nums):
            ans[i] = ans[i] * product
            product *= num
            
        return ans[::-1]