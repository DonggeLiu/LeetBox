"""
Question:
https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['({}){}'.format(left, right)
                for num in range(n)
                for left in self.generateParenthesis(num)
                for right in self.generateParenthesis(n-1-num)] if n else ['']