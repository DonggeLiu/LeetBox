"""
Question:
https://leetcode.com/problems/number-of-islands/description/
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) if grid else 0

        def mark(i, j):
            grid[i][j] = '0'
            if i > 0 and grid[i - 1][j] == '1':
                mark(i - 1, j)
            if j > 0 and grid[i][j - 1] == '1':
                mark(i, j - 1)
            if i < m - 1 and grid[i + 1][j] == '1':
                mark(i + 1, j)
            if j < n - 1 and grid[i][j + 1] == '1':
                mark(i, j + 1)
            return 1

        return sum(mark(i, j) for i in range(m) for j in range(n) if grid[i][j] == '1')
