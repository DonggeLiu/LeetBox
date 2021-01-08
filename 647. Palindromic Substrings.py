"""
Question:
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        c = r = 0
        s = "#" + "#".join(s) + "#"
        dp = [0] * len(s)
        num = 0
        for i in range(0, len(s)):
            if i < r:
                dp[i] = min(r - i, dp[2 * c - i])
            while (0 + dp[i] <= i < len(s) - dp[i]) and (s[i + dp[i]] == s[i - dp[i]]):
                dp[i] += 1
            if i + dp[i] > r:
                c, r = i, i + dp[i]
            num += dp[i] // 2
        return num
