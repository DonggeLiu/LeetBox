"""
Question
https://leetcode.com/problems/rotate-image/description/
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix) - 1

        for i in range(len(matrix)//2):
            for j in range(i, x-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[x-j][i]
                matrix[x-j][i] = matrix[x-i][x-j]
                matrix[x-i][x-j] = matrix[j][x-i]
                matrix[j][x-i] = tmp
