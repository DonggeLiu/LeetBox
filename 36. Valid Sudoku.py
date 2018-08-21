"""
Question:
https://leetcode.com/problems/valid-sudoku/description/
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic_row, dic_col, dic_box \
            = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell != ".":
                    if cell in dic_row[r] \
                            or cell in dic_col[c] \
                            or cell in dic_box[3 * (r // 3) + (c // 3)]:
                        return False
                    dic_row[r].add(cell)
                    dic_col[c].add(cell)
                    dic_box[3 * (r // 3) + (c // 3)].add(cell)
        return True
