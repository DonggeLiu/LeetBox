"""
Question:
https://leetcode.com/problems/optimal-division/
"""


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])

        s = str(nums[0]) + "/(" + str(nums[1])
        for num in nums[2:]:
            s += "/" + str(num)
        return s + ")"
