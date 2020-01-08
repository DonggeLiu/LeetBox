"""
Question
https://leetcode.com/problems/word-search/
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def match(m, n, x, board):
            if x == len(word):
                return True
            if m < 0 or n < 0 or m >= len(board) or n >= len(board[0]) or board[m][n] != word[x]:
                return False

            board[m][n] = None
            found = match(m - 1, n, x + 1, board) or match(m + 1, n, x + 1, board) or match(m,
                                                                                            n - 1,
                                                                                            x + 1,
                                                                                            board) or match(
                m, n + 1, x + 1, board)
            board[m][n] = word[x]
            return found

        if not word or not board or not board[0]:
            return False

        a = collections.Counter(c for row in board for c in row)
        b = collections.Counter(word)
        if b - a:
            return False

        M, N = len(board), len(board[0])
        for i in range(0, M):
            for j in range(0, N):
                if match(i, j, 0, board):
                    return True
        return False
