"""
Question:
https://leetcode.com/problems/4sum-ii/description/
"""


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        addend = collections.Counter([-(a+b) for a in A for b in B])
        return sum([addend[c+d] for c in C for d in D])
