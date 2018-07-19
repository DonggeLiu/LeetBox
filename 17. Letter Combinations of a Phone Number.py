"""
Question:
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        board = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        results = ['']
        for digit in digits:
            results = [result + c for result in results for c in board[digit]]
        return results if digits else []


"""
Recursion:
"""

# class Solution:
#     def __init__(self):
#         self.board = {str(i+1):string.ascii_lowercase[
#                                (i-1)*3 + (0 if i<7 else 1):
#                                (i-1)*3 + (3 if (i<6) else 4 if i<8 else 5)] for i in range(1,9)}
#
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if not digits:
#             return []
#         results = self.letterCombinations(digits[:-1])
#         return [result+c
#                 for result in (results if results else [''])
#                 for c in self.board[digits[-1]]]
