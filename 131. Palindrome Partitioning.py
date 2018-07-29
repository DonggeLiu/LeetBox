"""
Question:
https://leetcode.com/problems/palindrome-partitioning/description/
"""


class Solution:

    def partition(self, s):
        """
        Long but fastest
        :type s: str
        :rtype: List[List[str]]
        """
        results = [[s[0]]]
        for c in s[1:]:
            extra = []
            for r in results:
                r.append(c)
                if len(r) > 1:
                    p = ''.join(r[-2:])
                    if p == p[::-1]:
                        extra.append(r[:-2] + [p])
                    elif len(r) > 2:
                        p = ''.join(r[-3:])
                        if p == p[::-1]:
                            extra.append(r[:-3] + [p])
            results.extend(extra)
        return results

    def partition(self, s):
        """
        One-liner but extremely slow...
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:i]] + rest
                for i in range(1, len(s) + 1)
                if s[:i] == s[i - 1::-1]
                for rest in self.partition(s[i:])] or [[]]
