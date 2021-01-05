"""
Question:
https://leetcode.com/problems/minimum-time-difference/
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        times = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            bisect.insort(times, h * 60 + m)

        return min(
            min(abs(times[i - 1] - times[i]),
                24 * 60 - abs(times[i - 1] - times[i]))
            for i in range(len(times)))
