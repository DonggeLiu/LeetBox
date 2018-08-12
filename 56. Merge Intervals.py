"""
Question:
https://leetcode.com/problems/merge-intervals/description/
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if ans and ans[-1].end >= interval.start:
                ans[-1].end = max(ans[-1].end, interval.end)
            else:
                ans += interval,
        return ans
