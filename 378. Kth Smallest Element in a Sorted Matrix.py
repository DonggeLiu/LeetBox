"""
Question
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
"""


class Solution:
    def kthSmallest(self, matrix, k):
        """
        Not the fastest, but the most Pythonic
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return sorted([num for row in matrix for num in row])[k-1]
