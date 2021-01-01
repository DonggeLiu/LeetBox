"""
Question:
https://leetcode.com/problems/teemo-attacking/
"""


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = 0
        for i in range(len(timeSeries)):
            poisoned += min(duration, timeSeries[i] - timeSeries[i - 1]) if i else duration
        return poisoned
