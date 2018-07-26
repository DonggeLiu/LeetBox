"""
Question:
https://leetcode.com/problems/set-matrix-zeroes/description/
"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n, first_row_has_zero = len(matrix), len(matrix[0]), not all(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if not (matrix[i][0] and matrix[0][j]):
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
