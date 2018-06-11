"""
Question:
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
"""


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        
        rows_max = map(max, grid)
        cols_max = map(max, zip(*grid))

        return sum(min(row, col) for row in rows_max for col in cols_max) \
            - sum(map(sum, grid))
