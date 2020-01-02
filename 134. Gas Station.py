"""
Question
https://leetcode.com/problems/gas-station/
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, left, lack = 0, 0, 0
        for i in range(len(gas)):
            left += gas[i] - cost[i]
            if left < 0:
                start = i + 1
                lack += left
                left = 0
        return start if left + lack >= 0 else -1
