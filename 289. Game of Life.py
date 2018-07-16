"""
Question:
https://leetcode.com/problems/game-of-life/description/
"""


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def update_cell(i, j):
            count = sum([board[x][y] if type(board[x][y]) == int else not board[x][y]
                         for x in range(max(0, i-1), min(n, i+2))
                         for y in range(max(0, j-1), min(m, j+2)) if (x, y) != (i, j)])

            board[i][j] = False if board[i][j] and (count < 2 or count > 3) else \
                True if not board[i][j] and (count == 3) else board[i][j]

        def convert_cell(i, j):
            board[i][j] = int(board[i][j])

        n, m = len(board), len(board[0])
        [update_cell(i, j) for i in range(n) for j in range(m)]
        [convert_cell(i, j) for i in range(n) for j in range(m)]
