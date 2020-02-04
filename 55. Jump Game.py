"""
Question:
https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        furthest = len(nums) - 1
        for x in range(len(nums) - 2, -1, -1):
            if nums[x] + x >= furthest:
                furthest = x
            if furthest == 0:
                return True
        return False
