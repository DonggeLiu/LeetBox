"""
Question:
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c = min(set(s), key=s.count) if s else None
        return 0 if not c else \
            max(self.longestSubstring(t, k) for t in s.split(c)) if s.count(c) < k else len(s)
