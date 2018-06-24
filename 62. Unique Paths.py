"""
Question
https://leetcode.com/problems/unique-paths/description/
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from functools import reduce
        from operator import mul
        return reduce(mul, range(m, m+n-1), 1)//reduce(mul, range(1, n), 1)
