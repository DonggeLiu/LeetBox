"""
Questions:
https://leetcode.com/problems/third-maximum-number/
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_numbers = set(nums)
        maximum = max(unique_numbers)

        if len(unique_numbers) < 3:
            return maximum

        unique_numbers.remove(maximum)
        second_max = max(unique_numbers)
        unique_numbers.remove(second_max)
        return max(unique_numbers)
