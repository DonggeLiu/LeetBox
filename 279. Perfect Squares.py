"""
Question:
https://leetcode.com/problems/perfect-squares/description/
"""


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_square(val):
            return val**0.5 == int(val**0.5)
        def is_two_squares():
            return sum([is_square(n-i**2) for i in range(1, int(n**0.5)+1)])
        while not (n & 3):
            n >>= 2
        return 1 if is_square(n) else 4 if (n & 7) == 7 else 2 if is_two_squares() else 3
