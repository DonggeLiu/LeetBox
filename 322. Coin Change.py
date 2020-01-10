"""
Question
https://leetcode.com/problems/coin-change/
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mins = [float('inf')] * (amount+1)
        mins[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                mins[i] = min(mins[i], mins[i-coin]+1)
        return -1 if mins[amount] == float('inf') else mins[amount]
