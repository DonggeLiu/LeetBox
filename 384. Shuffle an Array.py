"""
Question:
https://leetcode.com/problems/shuffle-an-array/description/
"""


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._tem_nums = nums
        self._per_nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._per_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # Using random.sample is more elegant and only requires one private attribute
        # But it is generally slower than shuffle.
        random.shuffle(self._tem_nums)
        return self._tem_nums
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
