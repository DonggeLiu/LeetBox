"""
Question:
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def substr():
            if len(s) < len(x):
                return False
            start = 0
            for i in range(len(x)):
                start = s.find(x[i], start) + 1
                if not start or (len(s) - start < len(x) - i - 1):
                    return False
            return True

        max_len, max_str = 0, ""
        for x in d:
            if not substr():
                continue
            if len(x) > max_len or (len(x) == max_len and x < max_str):
                max_len, max_str = len(x), x
        return max_str
