"""
Question:
https://leetcode.com/problems/word-break/description/
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [not i for i in range(n + 1)]
        wd = set(wordDict)
        word_len_map = {word[-1]: set() for word in wordDict}
        for word in wordDict:
            word_len_map[word[-1]].add(len(word))

        for i in range(n):
            if s[i] in word_len_map:
                for j in word_len_map[s[i]]:
                    if dp[i + 1 - j] and (s[i + 1 - j:i + 1] in wd):
                        dp[i + 1] = True

        return dp[n]
