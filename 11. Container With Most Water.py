"""
Question:
https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, max_v = 0, len(height) - 1, 0

        while i < j:
            move_i = height[i] < height[j]
            short_l = height[i if move_i else j]
            max_v = max(short_l * (j - i), max_v)

            while i < j and height[i if move_i else j] <= short_l:
                i, j = (i + 1, j) if move_i else (i, j - 1)
        return max_v
